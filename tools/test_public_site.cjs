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
  '.css': 'text/css', '.gif': 'image/gif', '.png': 'image/png', '.md': 'text/plain' };
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
    await page.goto(base);
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
