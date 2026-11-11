(() => {
  'use strict';
  const KEY = 'awesome-ai-model-showcases-lang';
  function queryLang() {
    const q = new URLSearchParams(location.search).get('lang');
    if (q === 'en' || q === 'zh') return q;
    return '';
  }
  function detectLang() {
    const q = queryLang();
    if (q) return q;
    try {
      const stored = localStorage.getItem(KEY);
      if (stored === 'en' || stored === 'zh') return stored;
    } catch (e) { /* ignore */ }
    const nav = String(navigator.language || navigator.userLanguage || '').toLowerCase();
    return nav.startsWith('zh') ? 'zh' : 'en';
  }
  const I18N = {
    en: {
      skip: 'Skip to catalog',
      brand: 'Case library',
      brandAria: 'Awesome AI Model Showcases home',
      navCatalog: 'Catalog',
      navGifs: 'Real GIFs',
      navGame: 'Game sequences',
      navIdeas: 'Appendix · playbooks',
      navPopular: 'Appendix · popular',
      eyebrow: 'Community catalog · not a playbook showcase',
      heroTitle: 'Real cases from the public web.',
      heroLead: 'Awesome AI Model Showcases collects real public cases from the latest model families: original authors, posts, prompts, and credited videos. Homepage totals are Claude, Gemini, GPT-6.2 Sol, Grok, Qwen, and DeepSeek. The GPT Image GIF archive is the subproject collections/gpt-image-gifs and is not in that total. This is not this repository\'s original playbook showcase. Author claim is not official verification.',
      openCatalog: 'Open the catalog',
      markdown: 'Markdown table',
      realGifs: 'Local GIFs',
      mMain: 'Homepage cases',
      mX: 'Claude',
      mWeb: 'Gemini',
      mGame: 'GPT-6.2 Sol',
      mPending: 'Pending',
      mAppendix: 'Appendix (not success)',
      coverage: 'Coverage boundary',
      cov1: 'Officially verified 2.6 game outputs: 0',
      cov2: 'Main table is not “confirmed generation success”',
      cov3: 'Promo / 2.5 / multimodel / failure → appendix',
      cov4: 'Six local GIFs are seeds, not the collection',
      cov5: 'Twelve popular-GIF restages are not 2.6 works',
      catalogKicker: 'COMMUNITY CASES',
      catalogTitle: 'Case catalog',
      catalogHelp: 'Each row is an original post or source site. The homepage list is the frontier families. Promo, 2.5, and failures stay out. GPT Image GIFs are a separate subproject. Case text uses AI translations, not human-reviewed; open a case to compare its original.',
      searchCases: 'Search author, play, id…',
      emptyCases: 'No matching cases.',
      gifKicker: 'REAL GIFS ONLY',
      gifTitle: 'Real local GIFs',
      gifHelp: 'Only media with a documented publication grant plays here. Other entries link to the original source.',
      searchGifs: 'Search GIF titles, tags…',
      emptyGifs: 'No matching real GIFs.',
      faqKicker: 'FAQ',
      faqTitle: 'What this catalog is',
      whatIs: 'What is this repository?',
      whatIsBody: 'A community library of frontier-model cases: Claude, Gemini, GPT-6.2 Sol, Grok, Qwen, and DeepSeek. Each case keeps author, post, prompt (empty if unpublished), and a credited video when the source had one. GPT Image 2.6 GIFs are the subproject collections/gpt-image-gifs and are not in the homepage total. Not this site\'s original playbooks.',
      whatCan: 'What can I do with it?',
      whatCanBody: 'Open local media and full prompts, use original URLs as citations, submit another original-author case. Browsing does not call the Images API.',
      whatNot: 'What can it not do?',
      whatNotBody: 'No exhaustive-web claim, no official verification, no blanket author-grant or CC0 claim, no SVG-as-result. Appendix playbook/popular pages are Chinese-first and not a second inventory.',
      licenseH: 'What are the license boundaries?',
      licenseBody: 'MIT covers source code only. Third-party media stays license-unknown unless a specific grant is recorded per case. Follow credited licenses; no blanket CC0 grant. Stars or traffic are not a license.',
      langsH: 'Which languages are maintained?',
      langsBody: 'Four README editions share one catalog: English, Simplified Chinese, Traditional Chinese, and Japanese. Case content is translated too, with originals preserved and AI translations labeled as not human-reviewed. The catalog is English/Simplified Chinese; each case reader offers all four languages.',
      appendixKicker: 'APPENDIX',
      appendixTitle: 'Playbooks live on appendix pages.',
      appendixP: 'This-repo adaptations, Morphic cards (examples are not 2.6), and popular-GIF restages are not the main community list. Those appendix pages are Chinese-first and not claimed as a full English sync.',
      aIdeas: 'Appendix · playbooks & prompts',
      aPopular: 'Appendix · popular GIF restages (not 2.6)',
      aGame: 'Game sequences (verification labeled)',
      r1t: 'Submit a community case',
      r1p: 'Original post + media link + prompt or explicit empty + model evidence.',
      r2t: 'Do not mix buckets',
      r2p: '2.5, promo, failure, and this-repo playbooks go to the appendix.',
      r3t: 'Archive with attribution',
      r3p: 'Store source files under docs/cases/<id>/ and record the source license, or unknown.',
      r4t: 'No SVG as a result',
      r4p: 'Concept covers are never model outputs.',
      footL: 'Community case library ·',
      footR: 'Not affiliated with OpenAI. Third-party media is not MIT-licensed.',
      thAuthor: 'Author',
      thPlay: 'Play',
      thPost: 'Post',
      thMedia: 'Media',
      thPrompt: 'prompt',
      thModel: 'Model',
      thPipe: 'Pipeline',
      thVerify: 'Verification',
      thLicense: 'License',
      post: 'post',
      linkOnly: 'license unknown',
      licenseUnknown: 'license unknown',
      promptAtSource: 'Published at source', promptAggregator: 'Aggregator only',
      promptUnpublished: 'Unpublished', promptPartial: 'Short / partial', promptOriginal: 'Original',
      local: 'local',
      promptFull: 'full prompt',
      translation: 'translation',
      cite: 'source',
      groups: {
        main: 'Collected',
        x: 'X author-claimed',
        web: 'Non-X real GIFs',
        inrepo: 'In-repo longform',
        game: 'Game author-claimed',
        pending: 'Pending',
        appendix: 'Appendix (not success)',
        seeds: 'Repo seeds',
      },
    },
    zh: {
      skip: '跳到案例总表',
      brand: 'AI 模型制作案例集',
      brandAria: 'AI 模型制作案例集首页',
      navCatalog: '案例总目',
      navGifs: '真 GIF',
      navGame: '游戏序列',
      navIdeas: '附加·玩法',
      navPopular: '附加·热门',
      eyebrow: '社区收集库 · 不是本站方案展',
      heroTitle: '真实案例。',
      heroLead: 'AI 模型制作案例集收录最新模型家族的公开案例：原作者、原帖、提示词，以及署名后的视频副本。首页合计是 Claude、Gemini、GPT-6.2 Sol、Grok、Qwen、DeepSeek。GPT Image 的 GIF 归档在子项目 collections/gpt-image-gifs，不计入这个合计。作者声明不是官方验证。',
      openCatalog: '打开总目录',
      markdown: 'Markdown 总表',
      realGifs: '本地 GIF',
      mMain: '首页案例',
      mX: 'Claude',
      mWeb: 'Gemini',
      mGame: 'GPT-6.2 Sol',
      mPending: '待核',
      mAppendix: '附表非成功',
      coverage: '覆盖边界',
      cov1: '官方验证 2.6 游戏成品：0',
      cov2: '主表不是「已确认生成成功」',
      cov3: '平台宣传 / 2.5 / 多模型 / 失败 → 附表',
      cov4: '仓库 6 个本地 GIF = 种子，不是征集主清单',
      cov5: '热门 GIF 12 重演 = 附加参考，不是 2.6 作品',
      catalogKicker: 'COMMUNITY CASES',
      catalogTitle: '案例总目录',
      catalogHelp: '每行都是原帖或源站。首页列表是前沿家族。宣传、2.5、失败不混进来。GPT Image 的 GIF 在单独的子项目里。案例正文为 AI 译文，未经人工审校，打开案例可对照原文。',
      searchCases: '搜作者、玩法、id…',
      emptyCases: '没有匹配案例。',
      gifKicker: 'REAL GIFS ONLY',
      gifTitle: '真实本地 GIF',
      gifHelp: '仅播放有明确授权记录的素材；其余条目保留原帖入口。',
      searchGifs: '搜 GIF 标题、标签…',
      emptyGifs: '没有匹配的真 GIF。',
      faqKicker: 'FAQ',
      faqTitle: '这个目录是什么',
      whatIs: '这是什么仓库？',
      whatIsBody: '社区前沿模型案例库：Claude、Gemini、GPT-6.2 Sol、Grok、Qwen、DeepSeek。每条保留作者、原帖、提示词（未公开则空），来源有视频时保留署名副本。GPT Image 2.6 的 GIF 在子项目 collections/gpt-image-gifs，不计入首页合计。不是本站原创方案集。',
      whatCan: '这个目录能做什么？',
      whatCanBody: '打开本地媒体和完整 prompt、把原 URL 当出处、提交新的原作者案例。浏览不调用 Images API。',
      whatNot: '这个仓库做不到什么？',
      whatNotBody: '不宣称穷尽全网、不宣称官方验证、不声称全库已获授权或 CC0、不拿 SVG 充结果。玩法/热门附页以中文为主，不是第二套案例数。',
      licenseH: '许可边界是什么？',
      licenseBody: 'MIT 只覆盖源码。第三方媒体默认许可未知；明确授权按各案例标注，不代表全库 CC0。星数或访问量不是许可。',
      translation: '译文',
      langsH: '有哪些语言版本？',
      langsBody: '英文、简体中文、繁体中文、日文四份 README 共用一份目录。案例正文也提供 AI 译文，保留原文并标注未经人工审校。目录中英切换，案例译文阅读器支持四语。',
      appendixKicker: 'APPENDIX',
      appendixTitle: '方案与重演在附页。',
      appendixP: '本站改编、Morphic 提示词卡（示例非 2.6）、热门 GIF 重演不是社区成品主清单。这些附页以中文为主，不假装完整英文同步。',
      aIdeas: '附加·玩法与提示词',
      aPopular: '附加·热门 GIF 重演（不是 2.6）',
      aGame: '游戏序列（验证级别分开）',
      r1t: '交社区案例',
      r1p: '原帖 + 媒体外链 + prompt 原文或标明空 + 模型依据。',
      r2t: '不要混类',
      r2p: '2.5、宣传、失败、本站方案进附表。',
      r3t: '入库并标注出处',
      r3p: '文件放进 docs/cases/<id>/，记录来源许可；无明确授权时为未知。',
      r4t: '不拿 SVG 充结果',
      r4p: '概念封面永远不是模型成品。',
      footL: '社区案例收集库 ·',
      footR: '非 OpenAI 官方。第三方媒体不能因 MIT 自动商用。',
      thAuthor: '作者',
      thPlay: '玩法',
      thPost: '原帖',
      thMedia: '媒体',
      thPrompt: 'prompt',
      thModel: '模型依据',
      thPipe: '管线',
      thVerify: '验证',
      thLicense: '许可',
      post: '原帖',
      linkOnly: '许可未知',
      licenseUnknown: '许可未知',
      promptAtSource: '原文见来源', promptAggregator: '仅聚合页',
      promptUnpublished: '未公开', promptPartial: '短 / 部分', promptOriginal: '原文',
      local: '本地',
      promptFull: '全文 prompt',
      cite: '出处',
      groups: {
        main: '主表已收集',
        x: 'X 作者声明',
        web: '非X 真GIF',
        inrepo: '已在库长文',
        game: '游戏作者声明',
        pending: '待核',
        appendix: '附表（非成功）',
        seeds: '仓库种子',
      },
    },
  };
  function apply(lang) {
    const dict = I18N[lang] || I18N.en;
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      if (dict[key] != null) el.textContent = dict[key];
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (dict[key] != null) el.setAttribute('placeholder', dict[key]);
    });
    document.querySelectorAll('[data-i18n-aria]').forEach((el) => {
      const key = el.getAttribute('data-i18n-aria');
      if (dict[key] != null) el.setAttribute('aria-label', dict[key]);
    });
    const title = lang === 'zh'
      ? 'Awesome AI Model Showcases｜社区真实案例收集库'
      : 'Awesome AI Model Showcases — AI model GIF/animation cases by family';
    document.title = title;
    document.querySelectorAll('.lang-switch a').forEach((a) => {
      a.classList.toggle('active', a.getAttribute('data-lang') === lang);
    });
    window.UI_LANG = lang;
    window.UI_I18N = dict;
  }
  function setLang(lang) {
    if (lang !== 'en' && lang !== 'zh') return;
    try { localStorage.setItem(KEY, lang); } catch (e) { /* ignore */ }
    const url = new URL(location.href);
    url.searchParams.set('lang', lang);
    history.replaceState({}, '', url);
    apply(lang);
    document.dispatchEvent(new CustomEvent('ui-lang', { detail: lang }));
  }
  window.UI_LANG = detectLang();
  window.UI_I18N = I18N[window.UI_LANG];
  window.setUILang = setLang;
  document.addEventListener('DOMContentLoaded', () => {
    apply(window.UI_LANG);
    document.querySelectorAll('.lang-switch a').forEach((a) => {
      a.addEventListener('click', (ev) => {
        ev.preventDefault();
        setLang(a.getAttribute('data-lang'));
      });
    });
  });
})();
