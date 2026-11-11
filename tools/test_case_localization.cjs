const fs = require('fs'), vm = require('vm'), assert = require('node:assert/strict');
const catalog = JSON.parse(fs.readFileSync('docs/data/community-cases.json', 'utf8'));
const rows = Object.values(catalog).filter(Array.isArray).flat();
const record = rows.find(r => r.id === 'x-op7418-fatfish-pack');
function harness(id, lang) {
  const nodes = new Map();
  const el = id => { if (!nodes.has(id)) nodes.set(id, {textContent:'',hidden:true,href:'',setAttribute(k,v){this[k]=v;}}); return nodes.get(id); };
  const links = ['en','zh-CN','zh-TW','ja'].map(locale => ({href:'',getAttribute(){return locale;},setAttribute(k,v){this[k]=v;}}));
  const document = {getElementById: el, querySelectorAll(){return links;},documentElement:{lang:''},title:''};
  vm.runInNewContext(fs.readFileSync('docs/translated-case.js','utf8'), {window:{COMMUNITY_CASES:catalog}, document, URLSearchParams, location:{search:'?'+new URLSearchParams({id,lang})}});
  return {el,links,document};
}
for (const lang of ['en','zh-CN','zh-TW','ja']) {
  const {el,links,document} = harness(record.id, lang);
  assert.equal(document.documentElement.lang, lang);
  assert.equal(el('case-title').textContent, record.translations[lang].title);
  assert.equal(el('case-prompt').textContent, record.translations[lang].original_prompt);
  assert.equal(el('case-original-prompt').textContent, record.original_prompt);
  assert.equal(el('case-original-model').textContent, record.model_claim);
  assert.equal(el('case-source').href, record.source_url);
  assert.equal(el('case-content').hidden,false);
  assert.ok(links.every(a=>a.href.includes(record.id)));
  assert.equal(links.filter(a=>a['aria-current']==='page').length, 1);
}
const missing = harness('missing-record','ja');
assert.equal(missing.el('case-error').hidden,false);
assert.match(missing.el('case-error').textContent,/事例/);
const empty = rows.find(r => !r.original_prompt);
assert.match(harness(empty.id,'en').el('case-prompt').textContent,/No prompt text/);
const long = rows.find(r => (r.original_prompt||'').includes('<direction>'));
assert.equal(harness(long.id,'ja').el('case-original-prompt').textContent,long.original_prompt);
assert.equal(harness(record.id,'zh').document.documentElement.lang,'zh-CN');
assert.equal(harness(record.id,'invalid').document.documentElement.lang,'en');
console.log('translation reader ok: four locales, original preservation, empty prompts, invalid IDs, inert quoted text');
// The two-language catalog switches content as well as its UI, and searches both languages.
{
  const nodes = new Map(), callbacks = {};
  const el = id => {if(!nodes.has(id))nodes.set(id,{textContent:'',value:'',innerHTML:'',addEventListener(event,fn){this[event]=fn;},replaceChildren(){},append(){}});return nodes.get(id);};
  const window = {COMMUNITY_CASES:catalog, PUBLIC_MEDIA_PATHS:[], UI_LANG:'en'};
  const document = {getElementById:el, createElement:()=>el(Math.random()),addEventListener(event,fn){callbacks[event]=fn;},readyState:'complete'};
  vm.runInNewContext(fs.readFileSync('docs/cases-app.js','utf8'),{window,document,encodeURIComponent});
  const target = catalog.collected_by_family.claude.find(r=>r.title.includes('Indiranagar'));
  assert.ok(el('case-rows').innerHTML.includes(target.translations.en.title));
  assert.ok(el('case-rows').innerHTML.includes('translated-case.html?id='));
  window.UI_LANG='zh';callbacks['ui-lang']();
  assert.ok(el('case-rows').innerHTML.includes(target.translations['zh-CN'].title));
  el('case-search').value=target.translations.en.title;el('case-search').input();
  assert.equal(el('case-visible').textContent,'1');
  assert.ok(el('case-rows').innerHTML.includes(target.translations['zh-CN'].title));
}
console.log('localized catalog ok: translated rows, language switching, multilingual search');
