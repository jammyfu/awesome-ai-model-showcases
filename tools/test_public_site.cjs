/* Real browser check of the approved Pages artifact, with no external media. */
const { chromium } = require('playwright');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');

const repo = path.resolve(__dirname, '..');
const root = path.resolve(process.env.PUBLIC_SITE_DIR || path.join(repo, '_site'));
const catalog = JSON.parse(fs.readFileSync(path.join(repo, 'docs/data/community-cases.json'), 'utf8'));
const types = { '.html': 'text/html', '.js': 'application/javascript', '.json': 'application/json',
  '.css': 'text/css', '.gif': 'image/gif', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.md': 'text/plain' };
const server = http.createServer((req, res) => {
  let file = path.resolve(root, '.' + decodeURIComponent(req.url.split('?')[0]));
  if (file === root) file = path.join(root, 'index.html');
  if (file.startsWith(root + '/') && fs.existsSync(file) && fs.statSync(file).isDirectory()) {
    file = path.join(file, 'index.html');
  }
  if (!file.startsWith(root + '/') || !fs.existsSync(file)) {
    res.writeHead(404);
    return res.end('Not found');
  }
  res.setHeader('Content-Type', types[path.extname(file)] || 'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});

(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 960 } });
    const errors = [], externalMedia = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('request', request => {
      if (['image', 'media'].includes(request.resourceType()) && !request.url().startsWith(base + '/')) {
        externalMedia.push(request.url());
      }
    });
    // Full-width licensed galleries: every locale and mobile/desktop, not README DOM.
    for (const width of [320, 390, 768, 1280]) {
      await page.setViewportSize({ width, height: 900 });
      for (const lang of ['en', 'zh-CN', 'zh-TW', 'ja']) {
        await page.goto(base + '/licensed-gallery.' + lang + '.html');
        assert.equal(await page.locator('html').getAttribute('lang'), lang);
        assert.equal(await page.locator('article').count(), 8);
        for (const img of await page.locator('article img').all()) {
          await img.scrollIntoViewIfNeeded();
          await img.evaluate(el => el.decode());
          const box = await img.boundingBox();
          assert.ok(box.width >= Math.min(width - (width <= 480 ? 36 : 48), 952) - 1, 'Useful large preview width');
        }
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'Gallery must fit viewport');
        if (process.env.GALLERY_SCREENSHOTS) {
          fs.mkdirSync(process.env.GALLERY_SCREENSHOTS, { recursive: true });
          await page.screenshot({ path: path.join(process.env.GALLERY_SCREENSHOTS, `gallery-${lang}-${width}.jpg`), fullPage: true, type: 'jpeg', quality: 75 });
        }
        await page.getByRole('link', { name: 'DeepSeek', exact: true }).click();
        assert.match(page.url(), /#licensed-deepseek-crowned-frog$/);
        await page.locator('#licensed-deepseek-crowned-frog figure a').click();
        await page.waitForURL('**/licensed-deepseek-crowned-frog.png');
        await page.goBack();
        assert.equal(await page.locator('article').count(), 8);
        const other = lang === 'en' ? 'zh-CN' : 'en';
        await page.locator('nav[aria-label=Languages] a[lang="' + other + '"]').click();
        assert.equal(await page.locator('html').getAttribute('lang'), other);
      }
    }
    // All supported main-catalog UI locales at phone, tablet and desktop widths.
    for (const width of [320, 390, 768, 1280]) {
      await page.setViewportSize({ width, height: 900 });
      for (const lang of ['en', 'zh']) {
        await page.goto(base + '/?lang=' + lang);
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `Catalog overflow ${width}/${lang}`);
        for (const control of await page.locator('.nav a, .hero-actions a, #case-search').all()) {
          assert.ok(await control.isVisible(), 'Navigation must not vanish on phones');
          const box = await control.boundingBox();
          assert.ok(box.x >= 0 && box.x + box.width <= width + 1, 'Controls stay reachable within viewport');
        }
        await page.locator('#case-search').fill('dragon');
        assert.ok(await page.locator('#case-rows tr').count() > 0);
        if (process.env.GALLERY_SCREENSHOTS) {
          await page.locator('#case-rows tr').first().screenshot({ path: path.join(process.env.GALLERY_SCREENSHOTS, `record-${lang}-${width}.jpg`), type: 'jpeg', quality: 85 });
        }
        if (width <= 768) {
          const table = page.locator('.case-table');
          assert.ok(await table.evaluate(el => el.scrollWidth <= el.clientWidth + 1), 'Phone/tablet cases must not require a wide table');
          assert.ok(await page.locator('#case-rows td[data-label]').count() > 0);
        }
        await page.locator('#case-filters button').filter({ hasText: 'GPT Image' }).click();
        await page.locator('#case-search').fill('ailingqu');
        assert.equal(await page.locator('#case-rows tr').count(), 8);
        await page.locator('#case-search').fill('no-such-case-zzz');
        assert.equal(await page.locator('#case-rows tr').count(), 0);
        await page.locator('#case-search').fill('');
        if (process.env.GALLERY_SCREENSHOTS) {
          await page.screenshot({ path: path.join(process.env.GALLERY_SCREENSHOTS, `catalog-${lang}-${width}.jpg`), type: 'jpeg', quality: 75 });
        }
      }
      for (const route of ['/ideas.html', '/game.html', '/popular.html', '/translated-case.html?id=x-op7418-fatfish-pack&lang=ja']) {
        await page.goto(base + route);
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `Page overflow ${width}/${route}`);
      }
    }
    // Blocking one image must leave source and permission links reachable.
    await page.route('**/readme-assets/cases/licensed-deepseek-crowned-frog.png', route => route.abort());
    await page.goto(base + '/licensed-gallery.en.html#licensed-deepseek-crowned-frog');
    const frog = page.locator('#licensed-deepseek-crowned-frog');
    assert.ok(await frog.getByRole('link', { name: 'Source', exact: true }).isVisible());
    assert.ok(await frog.getByRole('link', { name: 'Permission', exact: true }).isVisible());
    await page.unroute('**/readme-assets/cases/licensed-deepseek-crowned-frog.png');
    await page.setViewportSize({ width: 1280, height: 960 });
    await page.goto(base);
    for (const selector of ['.showcase-banner', '.source-spotlight .spotlight-locale:visible img']) {
      await page.locator(selector).evaluate(image => image.decode());
      assert.ok(await page.locator(selector).evaluate(image => image.naturalWidth >= 1600));
    }
    assert.match(await page.locator('.source-spotlight .spotlight-locale:visible').innerText(), /Claude Opus 5.5/);
    assert.ok((await page.locator('.source-spotlight').boundingBox()).y < 960, 'Actual work should appear in the desktop first screen');
    assert.equal(await page.locator('#case-rows tr').count(), catalog.meta.counts.main_collected);
    assert.equal(await page.locator('video').count(), 0);
    assert.equal(await page.locator('#case-rows img').count(), 0);
    await page.locator('#case-search').fill('motion');
    assert.ok(await page.locator('#case-rows tr').count() > 0);
    await page.locator('#case-search').fill('');
    await page.locator('#case-filters button').filter({ hasText: 'GPT Image' }).click();
    assert.equal(await page.locator('#case-rows tr').count(), catalog.meta.counts.gpt_image);
    assert.equal(await page.locator('#case-rows img').count(), 8);
    for (const image of await page.locator('#case-rows img').all()) {
      await image.scrollIntoViewIfNeeded();
      await image.evaluate(element => element.decode());
      assert.ok(await image.evaluate(element => element.naturalWidth > 0));
    }
    await page.locator('#case-search').fill('ailingqu');
    assert.equal(await page.locator('#case-rows tr').count(), 8);
    await page.locator('#case-search').fill('rice');
    assert.equal(await page.locator('#case-rows img').count(), 0);

    const rows = Object.values(catalog).flatMap(value => Array.isArray(value) ? value : []);
    const ids = [...new Set(rows.filter(row => row.local_page?.endsWith('index.html')).map(row => row.id))];
    let animatedGifs = 0;
    for (const id of ids) {
      await page.goto(base + '/cases/' + id + '/');
      const media = page.locator('img,video');
      if (id.startsWith('ailingqu-')) {
        assert.equal(await media.count(), 1);
        await media.first().evaluate(element => element.decode());
        const first = await media.first().screenshot();
        let moved = false;
        for (let attempt = 0; attempt < 8 && !moved; attempt++) {
          await page.waitForTimeout(170);
          moved = !first.equals(await media.first().screenshot());
        }
        assert.ok(moved, `${id}: approved GIF must visibly animate, not just return HTTP 200`);
        animatedGifs++;
      } else {
        assert.equal(await media.count(), 0, id);
      }
      assert.ok(await page.getByText('View original source / 查看原帖', { exact: true }).count());
    }
    for (const route of ['/ideas.html', '/game.html', '/popular.html']) {
      await page.goto(base + route);
      assert.equal(await page.locator('img,video').count(), 0, route);
    }
    const translated = rows.find(row => row.id === 'x-op7418-fatfish-pack');
    for (const lang of ['en', 'zh-CN', 'zh-TW', 'ja']) {
      await page.goto(base + '/translated-case.html?' + new URLSearchParams({id: translated.id, lang}));
      assert.equal(await page.locator('html').getAttribute('lang'), lang);
      assert.equal(await page.locator('#case-title').textContent(), translated.translations[lang].title);
      assert.equal(await page.locator('#case-prompt').textContent(), translated.translations[lang].original_prompt);
      await page.locator('#original-content summary').click();
      assert.equal(await page.locator('#case-original-prompt').textContent(), translated.original_prompt);
      await page.locator('[data-locale="en"]').click();
      assert.equal(await page.locator('html').getAttribute('lang'), 'en');
      assert.equal(new URL(page.url()).searchParams.get('id'), translated.id);
    }
    await page.goto(base + '/translated-case.html?id=unknown&lang=ja');
    assert.ok(await page.locator('#case-error').isVisible());
    assert.equal(await page.locator('#case-content').isVisible(), false);
    assert.equal(animatedGifs, 8);
    // Source links remain available even if the permitted preview fails to load.
    await page.route('**/cases/ailingqu-jelly-bear-wobble/media/01-gif.gif', route => route.abort());
    await page.goto(base + '/cases/ailingqu-jelly-bear-wobble/');
    assert.ok(await page.getByText('View original source / 查看原帖', { exact: true }).isVisible());
    await page.unroute('**/cases/ailingqu-jelly-bear-wobble/media/01-gif.gif');
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(base);
    assert.ok((await page.locator('.source-spotlight').boundingBox()).y < 844, 'Actual work should start in the mobile first screen');
    assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'No horizontal page overflow');
    await page.locator('[data-lang="zh"]').click();
    assert.equal(await page.locator('[data-gallery-link]').getAttribute('href'), 'licensed-gallery.zh-CN.html');
    assert.equal(await page.locator('.source-spotlight .spotlight-locale:visible').getAttribute('lang'), 'zh-CN');
    assert.match(await page.locator('.source-spotlight .spotlight-locale:visible').innerText(), /让城市生长/);
    await page.locator('[data-lang="en"]').click();
    await page.route('**/readme-assets/cases/03-isometric.jpg', route => route.abort());
    await page.goto(base);
    assert.ok(await page.locator('.source-spotlight .spotlight-locale:visible').getByRole('link', { name: 'Watch →', exact: true }).isVisible());
    await page.unroute('**/readme-assets/cases/03-isometric.jpg');
    assert.equal(await page.locator('#case-rows tr').count(), catalog.meta.counts.main_collected);
    await page.locator('#case-search').fill('motion');
    assert.ok(await page.locator('#case-rows tr').count() > 0);
    await page.locator('#case-search').fill('');
    assert.deepEqual(errors, []);
    assert.deepEqual(externalMedia, []);
    console.log(JSON.stringify({ homepageCases: catalog.meta.counts.main_collected,
      gptImageCases: catalog.meta.counts.gpt_image, approvedBrowserGifs: 8,
      casePagesChecked: ids.length, animatedGifs, gifAnimation: 'changing rendered frames observed for all approved GIFs',
      mobileViewport: '390x844', failedPreviewSourceFallback: 'passed',
      unknownVideoElements: 0, externalMediaRequests: 0, consoleErrors: 0 }, null, 2));
  } finally {
    await browser.close();
    server.close();
  }
})().catch(error => { console.error(error); server.close(); process.exit(1); });
