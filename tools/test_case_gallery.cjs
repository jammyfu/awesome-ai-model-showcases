const fs=require('fs'), vm=require('vm'), assert=require('node:assert/strict');
const nodes=new Map();
const el=id=>{if(!nodes.has(id))nodes.set(id,{textContent:'',value:'',innerHTML:'',addEventListener(){},replaceChildren(){},append(){}});return nodes.get(id)};
const rows=[
{id:'licensed',prompt_status:'有原文',local_prompt:'docs/cases/a/prompt.md',license_label:'CC BY 4.0',license_url:'https://creativecommons.org/licenses/by/4.0/'},
{id:'source',prompt_status:'source_only',prompt_url:'https://example.org/prompt'},
{id:'aggregator',prompt_status:'aggregator_only',prompt_url:'https://example.org/secondary'},
{id:'empty',prompt_status:'空',local_prompt:'docs/cases/b/prompt.md'},
{id:'partial',prompt_status:'短/部分',local_prompt:'docs/cases/c/prompt.md'}];
const catalog={meta:{counts:{}},collected_x_author_claim:[],collected_web_gif:rows,collected_already_in_repo:[],collected_game_author_claim:[],pending:[],prompt_only:[],excluded:[],appendix:[],repo_seeds:[]};
vm.runInNewContext(fs.readFileSync('docs/cases-app.js','utf8'),{window:{COMMUNITY_CASES:catalog},document:{getElementById:el,createElement:()=>el(Math.random()),addEventListener(){},readyState:'complete'}});
const html=el('case-rows').innerHTML;
assert.match(html,/href="https:\/\/example.org\/prompt"[^>]*>Published at source</);
assert.match(html,/href="https:\/\/example.org\/secondary"[^>]*>Aggregator only</);
for(const label of ['CC BY 4.0','Unpublished','Short / partial'])assert.ok(html.includes('>'+label+'<'));
console.log('gallery smoke ok: source links, prompt scope and license');
