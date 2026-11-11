(() => {
  'use strict';
  const labels = {
    en: ['Catalog', 'Author', 'Original source', 'AI translation, not human-reviewed. Compare with the original. Translation does not verify a model claim, reproduce a result, or grant reuse rights.', 'Method', 'Verification', 'Model evidence (translation)', 'Published prompt (translation)', 'Read the original', 'Original title', 'Original model evidence', 'Original prompt', 'Source rights (original)', 'No prompt text was collected. See the source; no prompt has been invented.', 'Case not found. Return to the catalog.'],
    'zh-CN': ['目录', '作者', '原帖', 'AI 译文，未经人工审校，请对照原文。翻译不等于核实模型声明、复现结果或授予再利用许可。', '做法', '核验状态', '模型依据（译文）', '公开提示词（译文）', '查看原文', '原始标题', '模型依据原文', '原始提示词', '来源许可（原文）', '未收集到提示词正文。请查看来源，未编造提示词。', '未找到案例，请返回目录。'],
    'zh-TW': ['目錄', '作者', '原帖', 'AI 譯文，未經人工審校，請對照原文。翻譯不等於核實模型聲明、重現結果或授予再利用許可。', '做法', '核驗狀態', '模型依據（譯文）', '公開提示詞（譯文）', '查看原文', '原始標題', '模型依據原文', '原始提示詞', '來源許可（原文）', '未收集到提示詞內文。請查看來源，未編造提示詞。', '未找到案例，請返回目錄。'],
    ja: ['カタログ', '作者', '原投稿', 'AI 翻訳であり、人による校閲は未実施です。原文と比較してください。翻訳はモデルの主張の検証、結果の再現、再利用の許諾を意味しません。', '制作方法', '検証状況', 'モデルの根拠（翻訳）', '公開プロンプト（翻訳）', '原文を読む', '元のタイトル', 'モデルの根拠の原文', '元のプロンプト', '出典の権利表記（原文）', 'プロンプト本文は収集されていません。出典をご確認ください。プロンプトの補作はしていません。', '事例が見つかりません。カタログに戻ってください。'],
  };
  const query = new URLSearchParams(location.search);
  const requested = query.get('lang') === 'zh' ? 'zh-CN' : query.get('lang');
  const lang = Object.hasOwn(labels, requested) ? requested : 'en';
  const l = labels[lang];
  const set = (id, text) => { document.getElementById(id).textContent = text || ''; };
  const catalog = window.COMMUNITY_CASES || {};
  const record = Object.values(catalog).filter(Array.isArray).flat().find(r => r.id === query.get('id'));
  document.documentElement.lang = lang;
  document.querySelectorAll('[data-locale]').forEach(a => {
    const locale = a.getAttribute('data-locale');
    const next = new URLSearchParams({id: query.get('id') || '', lang: locale});
    a.href = `?${next}`;
    if (locale === lang) a.setAttribute('aria-current', 'page');
  });
  set('catalog-link', '← ' + l[0]);
  document.getElementById('catalog-link').href = `index.html?lang=${lang.startsWith('zh') ? 'zh' : 'en'}`;
  if (!record || !record.translations || !record.translations[lang]) {
    set('case-error', l[14]);
    document.getElementById('case-error').hidden = false;
    return;
  }
  const t = record.translations[lang];
  document.title = `${t.title} · Awesome AI Model Showcases`;
  for (const [id, index] of [['author-label',1], ['case-source',2], ['translation-notice',3], ['method-label',4], ['verification-label',5], ['model-label',6], ['prompt-label',7], ['original-label',8], ['original-title-label',9], ['original-model-label',10], ['original-prompt-label',11], ['rights-label',12]]) set(id, l[index]);
  set('case-title', t.title);
  set('case-author', record.author);
  set('case-method', t.pipeline);
  set('case-verification', t.verify);
  set('case-model', t.model_claim);
  set('case-prompt', t.original_prompt || l[13]);
  set('case-original-title', record.title);
  set('case-original-model', record.model_claim);
  set('case-original-prompt', record.original_prompt || l[13]);
  set('case-rights', record.license_notes);
  const archived = record.local_page || '';
  if (/^docs\/cases\/[a-zA-Z0-9_-]+\/index\.html$/.test(archived)) {
    const a = document.getElementById('case-archive');
    a.textContent = {en:'Archived case and approved media', 'zh-CN':'归档案例与获准展示的媒体', 'zh-TW':'歸檔案例與獲准展示的媒體', ja:'収録事例と公開許諾済みメディア'}[lang];
    a.href = archived.replace(/^docs\//, '');
    a.hidden = false;
  }
  // Keep every piece of collected text inert, including XML/code in long prompts.
  if (/^https?:\/\//.test(record.source_url || '')) document.getElementById('case-source').href = record.source_url;
  document.getElementById('case-content').hidden = false;
})();
