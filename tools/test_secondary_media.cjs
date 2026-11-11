const fs = require('fs'), vm = require('vm'), assert = require('node:assert/strict');
// Run the real renderers with a minimal DOM; removing their media gate must fail.
function run(file, records, allowed) {
  class Element {
    constructor(tag) { this.tagName = tag.toUpperCase(); this.children = []; this.value = ''; this.textContent = ''; this.options = []; this.classList = {add(){}, remove(){}}; this.listeners = {}; }
    append(...nodes) { this.children.push(...nodes); }
    replaceChildren(...nodes) { this.children = nodes; }
    setAttribute(k,v) { this[k] = v; }
    addEventListener(k,v) { this.listeners[k] = v; }
  }
  const nodes = new Map();
  const get = id => { if (!nodes.has(id)) nodes.set(id,new Element('div')); return nodes.get(id); };
  for (const id of ['category','origin','media','status','bucket']) get(id).value = 'all';
  const window = {GALLERY_ITEMS:records, GIF_IDEAS:records, POPULAR_PLAYBOOKS:{items:records}, addEventListener(){}};
  if (allowed !== undefined) window.PUBLIC_MEDIA_PATHS = allowed;
  vm.runInNewContext(fs.readFileSync(file,'utf8'), {window, document:{getElementById:get, createElement:t=>new Element(t), createTextNode:t=>({textContent:t}), addEventListener(){}}, location:{hash:'',search:''}, URLSearchParams, setTimeout,clearTimeout});
  const walk = n => [n,...n.children?.flatMap(walk)||[]];
  return {all:walk(get('cards')), get};
}
const base = {title:'Demo',title_zh:'Demo',description:'Description',description_zh:'Description',category:'Test',tags:[],storage:'external',rights:'unknown_link_only',frames:2,duration_ms:100,prompt:'Keep this prompt',game_sequence:true,media_kind:'gif',preview_kind:'external_gif',source_url:'https://example.org/post',original_gif_page:'https://example.org/post',evidence_url:'https://example.org/chart'};
const files = ['docs/app.js','docs/ideas-app.js','docs/game-app.js'];
for (const file of files) {
  for (const path of ['gifs/seed.gif','https://example.org/unlicensed.gif','//example.org/unlicensed.gif','cases/ok.gif?copy=1','../cases/ok.gif']) {
    const r = run(file,[{...base,image:path,preview:path,media_url:path,media_poster_url:path,reference_image_url:path,related_media_urls:[path]}],['cases/ok.gif']);
    assert.equal(r.all.filter(n=>['IMG','VIDEO','IFRAME','SOURCE'].includes(n.tagName)).length,0,`${file} must not embed ${path}`);
    assert.ok(r.all.some(n=>n.tagName==='A'&&n.href===base.source_url),`${file} must retain source CTA`);
    assert.ok(!r.all.some(n=>n.tagName==='A'&&n.href===path),`${file} must not substitute a direct-media link`);
  }
  const missing = run(file,[{...base,image:'cases/ok.gif',media_url:'cases/ok.gif'}]);
  assert.equal(missing.all.filter(n=>n.tagName==='IMG'||n.tagName==='VIDEO').length,0,`${file} fails closed without registry`);
  const good = run(file,[{...base,image:'cases/ok.gif',media_url:'cases/ok.gif',preview:'cases/ok.gif'}],['cases/ok.gif']);
  assert.ok(good.all.some(n=>n.tagName==='IMG'&&n.src==='cases/ok.gif'),`${file} authorized GIF`);
  good.get('search').value='no matching title'; good.get('search').listeners.input();
  assert.equal(good.get('cards').children.length,0,`${file} search remains functional`);
}
for (const file of files.slice(1)) {
  const r = run(file,[{...base,media_kind:'mp4',media_url:'cases/ok.mp4',media_poster_url:'https://example.org/unknown.jpg'}],['cases/ok.mp4']);
  assert.ok(r.all.some(n=>n.tagName==='VIDEO'&&n.src==='cases/ok.mp4'&&n.controls),`${file} authorized video with controls`);
  assert.ok(!r.all.some(n=>n.src==='https://example.org/unknown.jpg'));
}
const popular = run('docs/popular-app.js',[{...base,preview:'https://example.org/unknown.gif'}],[]);
assert.equal(popular.all.filter(n=>['IMG','VIDEO','IFRAME'].includes(n.tagName)).length,0);
assert.ok(popular.all.some(n=>n.href===base.original_gif_page));
console.log('secondary media: unknown embeds/links blocked, approved GIF/video, source CTAs and search pass');
// Production inventories also fail closed, including the six repository seed GIFs.
for (const [file, dataFile] of [
  ['docs/app.js','docs/data/gallery.json'],
  ['docs/ideas-app.js','docs/data/ideas.json'],
  ['docs/game-app.js','docs/data/ideas.json'],
  ['docs/popular-app.js','docs/data/popular-playbooks.json']
]) {
  const data = JSON.parse(fs.readFileSync(dataFile,'utf8'));
  const records = Array.isArray(data) ? data : data.items;
  const result = run(file, records, []);
  assert.equal(result.all.filter(n=>['IMG','VIDEO','SOURCE','IFRAME'].includes(n.tagName)).length, 0, `${file} real inventory has no unapproved embed`);
  assert.ok(result.get('cards').children.length > 0, `${file} retains catalog cards`);
}
console.log('secondary media: actual legacy inventories remain browsable without unauthorized media');
