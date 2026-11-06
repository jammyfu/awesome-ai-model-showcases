(() => {
  'use strict';
  const KEY = 'awesome-gpt-image-gifs-lang';
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
      brandAria: 'Awesome GPT Image GIFs home',
      navCatalog: 'Catalog',
      navGifs: 'Real GIFs',
      navGame: 'Game sequences',
      navIdeas: 'Appendix · playbooks',
      navPopular: 'Appendix · popular',
      eyebrow: 'Community catalog · not a playbook showcase',
      heroTitle: 'Real cases from the public web.',
      heroLead: 'Awesome GPT Image GIFs collects real GPT Image GIF cases from the public web: original authors, original media, public prompts, sources, and production pipelines. It is a community catalog of GPT Image 2.6 work, not this repository\'s original playbook showcase. Current public inventory, not exhaustive. Author claim ≠ official verification. X “GIF” attachments are usually unwatched MP4. Media is archived locally; original URLs are citations. License unknown — not an author grant.',
      openCatalog: 'Open the catalog',
      markdown: 'Markdown table',
      realGifs: 'Local GIFs',
      mMain: 'Collected',
      mX: 'X author-claimed',
      mWeb: 'Non-X real GIFs',
      mGame: 'Game author-claimed',
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
      catalogHelp: 'Each row is an original post or source site. Default main table: X25 + non-X12 + Luffy/Krouxzz + 4 game author-claims. Promo, 2.5, and failures stay out.',
      searchCases: 'Search author, play, id…',
      emptyCases: 'No matching cases.',
      gifKicker: 'REAL GIFS ONLY',
      gifTitle: 'Real local GIFs',
      gifHelp: 'Real GIFs only, no SVG. Collected source GIFs play from local archives. Repository seeds appear when you choose Local.',
      searchGifs: 'Search GIF titles, tags…',
      emptyGifs: 'No matching real GIFs.',
      faqKicker: 'FAQ',
      faqTitle: 'What this catalog is',
      whatIs: 'What is this repository?',
      whatIsBody: 'A community library of original-author GPT Image 2.6 cases: author, post, real GIF or MP4, public prompt (empty if missing), model evidence, native GIF vs sprite/postprocess, verification. Not this site\'s original playbooks.',
      whatCan: 'What can I do with it?',
      whatCanBody: 'Open local media and full prompts, use original URLs as citations, submit another original-author case. Browsing does not call the Images API.',
      whatNot: 'What can it not do?',
      whatNotBody: 'No exhaustive-web claim, no official verification, no author-grant or CC0 claim, no SVG-as-result. Appendix playbook/popular pages are Chinese-first and not a second inventory.',
      licenseH: 'What are the license boundaries?',
      licenseBody: 'MIT covers source code only. Archived third-party media stays license-unknown. Not an author grant or CC0. Stars or traffic are not a license.',
      langsH: 'Which languages are maintained?',
      langsBody: 'English and Simplified Chinese share one catalog JSON. No other README editions exist.',
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
      r3p: 'Store files under docs/cases/<id>/ and keep license unknown.',
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
      local: 'local',
      promptFull: 'full prompt',
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
      brand: '案例收集库',
      brandAria: '案例收集库首页',
      navCatalog: '案例总目',
      navGifs: '真 GIF',
      navGame: '游戏序列',
      navIdeas: '附加·玩法',
      navPopular: '附加·热门',
      eyebrow: '社区收集库 · 不是本站方案展',
      heroTitle: '真实案例。',
      heroLead: 'Awesome GPT Image GIFs 收集全网 GPT Image GIF 真实案例、原作者、原媒体、提示词、出处与制作流程；不是本站原创方案集。当前公开搜集核实清单，不是穷尽全网。作者声明 ≠ 官方验证。X 标 GIF 多为未观看 MP4。主表媒体已本地归档，原 URL 只作出处。许可未知，不是作者授权。',
      openCatalog: '打开总目录',
      markdown: 'Markdown 总表',
      realGifs: '本地 GIF',
      mMain: '主表已收集',
      mX: 'X 作者声明',
      mWeb: '非X 真 GIF',
      mGame: '游戏作者声明',
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
      catalogHelp: '每行都是社区原帖或源站。默认主表：X25 + 非X12 + 路飞/Krouxzz + 游戏作者声明4。不把宣传、2.5、失败混进来。',
      searchCases: '搜作者、玩法、id…',
      emptyCases: '没有匹配案例。',
      gifKicker: 'REAL GIFS ONLY',
      gifTitle: '真实本地 GIF',
      gifHelp: '只放真 GIF，不放 SVG。已收集的源站 GIF 从本地归档播放。仓库种子需点 Local 才出现。',
      searchGifs: '搜 GIF 标题、标签…',
      emptyGifs: '没有匹配的真 GIF。',
      faqKicker: 'FAQ',
      faqTitle: '这个目录是什么',
      whatIs: '这是什么仓库？',
      whatIsBody: '社区原作者 GPT Image 2.6 真实案例库：作者、原帖、真 GIF 或 MP4、公开 prompt（缺则空）、模型依据、直出还是切帧/后处理、验证级别。不是本站原创方案集。',
      whatCan: '这个目录能做什么？',
      whatCanBody: '打开本地媒体和完整 prompt、把原 URL 当出处、提交新的原作者案例。浏览不调用 Images API。',
      whatNot: '这个仓库做不到什么？',
      whatNotBody: '不宣称穷尽全网、不宣称官方验证、不声称已获授权或 CC0、不拿 SVG 充结果。玩法/热门附页以中文为主，不是第二套案例数。',
      licenseH: '许可边界是什么？',
      licenseBody: 'MIT 只覆盖源码。入库第三方媒体保持许可未知，不是作者授权或 CC0。星数或访问量不是许可。',
      langsH: '有哪些语言版本？',
      langsBody: '英文与简体中文共用一份目录 JSON。没有其他已维护 README。',
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
      r3p: '文件放进 docs/cases/<id>/，许可保持未知。',
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
      ? 'Awesome GPT Image GIFs｜社区真实案例收集库'
      : 'Awesome GPT Image GIFs — community catalog of real GPT Image GIF cases';
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
