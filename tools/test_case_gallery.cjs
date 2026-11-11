const fs=require('fs'), vm=require('vm'), assert=require('node:assert/strict');
const nodes=new Map();
const el=id=>{if(!nodes.has(id))nodes.set(id,{textContent:'',value:'',innerHTML:'',addEventListener(){},replaceChildren(){},append(){}});return nodes.get(id)};
const rows=[
{id:'unknown-media',source_url:'https://example.org/source-post',license_label:'CC BY 4.0',local_files:[{path:'docs/cases/unknown/media/leak.gif',ext:'gif'}],thumb:'https://example.org/leak.jpg',video:'docs/cases/unknown/media/leak.mp4',media_url:'https://example.org/leak.mp4'},
{id:'approved-video',source_url:'https://example.org/video-post',local_files:[{path:'docs/cases/approved/media/test.mp4',ext:'mp4',public_allowed:true}]},
{id:'stale-flag',local_files:[{path:'docs/cases/stale/media/stale.gif',ext:'gif',public_allowed:true}]},
{id:'unsafe-path',source_url:'https://example.org/unsafe',local_files:[{path:'https://example.org/remote.gif',ext:'gif',public_allowed:true},{path:'docs/../secret.gif',ext:'gif',public_allowed:true}]},
{id:'licensed',prompt_status:'有原文',local_prompt:'docs/cases/a/prompt.md',license_label:'CC BY 4.0',license_url:'https://creativecommons.org/licenses/by/4.0/'},
{id:'source',prompt_status:'source_only',prompt_url:'https://example.org/prompt'},
{id:'aggregator',prompt_status:'aggregator_only',prompt_url:'https://example.org/secondary'},
{id:'empty',prompt_status:'空',local_prompt:'docs/cases/b/prompt.md'},
{id:'partial',prompt_status:'短/部分',local_prompt:'docs/cases/c/prompt.md'}];
const catalog={meta:{counts:{}},collected_by_family:{claude:rows,gemini:[],'gpt-code':[],grok:[],qwen:[],deepseek:[],'gpt-image':[]},collected_x_author_claim:[],collected_web_gif:[],collected_already_in_repo:[],collected_game_author_claim:[],pending:[],prompt_only:[],excluded:[],appendix:[],repo_seeds:[]};
vm.runInNewContext(fs.readFileSync('docs/cases-app.js','utf8'),{window:{COMMUNITY_CASES:catalog,PUBLIC_MEDIA_PATHS:['cases/approved/media/test.mp4']},document:{getElementById:el,createElement:()=>el(Math.random()),addEventListener(){},readyState:'complete'}});
const html=el('case-rows').innerHTML;
assert.match(html,/href="https:\/\/example.org\/prompt"[^>]*>Published at source</);
assert.match(html,/href="https:\/\/example.org\/secondary"[^>]*>Aggregator only</);
for(const label of ['CC BY 4.0','Unpublished','Short / partial'])assert.ok(html.includes('>'+label+'<'));
assert.ok(!html.includes('leak.gif') && !html.includes('leak.mp4') && !html.includes('leak.jpg'));
assert.ok(!html.includes('stale.gif'));
assert.ok(!html.includes('remote.gif') && !html.includes('secret.gif'));
assert.match(html,/<video[^>]+src="cases\/approved\/media\/test.mp4"[^>]+controls/);
assert.ok(html.includes('https://example.org/source-post') && html.includes('https://example.org/video-post'));
console.log('gallery smoke ok: source links, prompt scope and license');
