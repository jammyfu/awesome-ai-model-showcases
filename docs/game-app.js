(() => {
  'use strict';
  // Fail closed: only exact docs-relative paths from the verified build registry.
  const publicMedia = new Set(Array.isArray(window.PUBLIC_MEDIA_PATHS) ? window.PUBLIC_MEDIA_PATHS : []);
  function approvedMedia(path) {
    return typeof path === 'string' && !/[:?#\\]/.test(path) && !path.startsWith('/') &&
      !path.split('/').some((part) => !part || part === '.' || part === '..') && publicMedia.has(path);
  }
  const all = Array.isArray(window.GIF_IDEAS) ? window.GIF_IDEAS : [];
  const items = all.filter((x) => x.game_sequence);
  const cards = document.getElementById('cards');
  const query = document.getElementById('search');
  const status = document.getElementById('status');
  const history = document.getElementById('history');
  const failures = document.getElementById('failures');
  const count = document.getElementById('visible');
  const empty = document.getElementById('empty');
  const toast = document.getElementById('toast');
  const authorN = items.filter((x) => (x.tags || []).includes('x-original-author')).length;
  const promoN = items.filter((x) => x.image26_status === 'promo_claim_unwatched').length;
  const failN = items.filter((x) => x.image26_status === 'failure_sample').length;
  const elA = document.getElementById('authorN');
  const elP = document.getElementById('promoN');
  const elF = document.getElementById('failN');
  if (elA) elA.textContent = String(authorN);
  if (elP) elP.textContent = String(promoN);
  if (elF) elF.textContent = String(failN);
  const statusLabel = {
    author_claim_unverified: '原作者声明 2.6 · 非官方验证',
    multimodel_postprocess: '含其他模型后处理 · 不是纯 2.6',
    promo_claim_unwatched: '宣传方 1 组 · 未观看',
    not_26: 'GPT Image 2.5 · 不是 2.6',
    failure_sample: '失败样本 · 不计成功',
  };
  const engineLabel = {
    none: '无引擎导入证据',
    documented_not_run: '有导入步骤 · 作者未实机跑',
    author_claim_unwatched: '作者宣称游戏演示 · 本仓未观看未运行',
    discussed_not_shown: '讨论过引擎 · 未见运行画面',
  };
  const alphaLabel = {
    solid_white_then_key_not_true_alpha: '白底再抠色 · 不是真 alpha',
    keyed_white_not_true_alpha: '白底抠色 · 不是真 alpha',
    opaque_author_setting_not_true_alpha: '作者用不透明底 · 不是真 alpha',
    gif_1bit_if_native_gif_unknown_here: '若是原生 GIF 多为 1-bit 透明 · 此处未核',
    unknown_sheet_then_agent: 'sheet 后由 agent 切帧 · 透明通道未核',
    author_mentions_transparent_unverified: '作者提到透明底 · 未核',
    unknown_pixel_grid: '像素格透明通道未核',
  };
  let t;
  function say(s) {
    toast.textContent = s;
    toast.classList.add('show');
    clearTimeout(t);
    t = setTimeout(() => toast.classList.remove('show'), 1900);
  }
  function el(tag, cl, text) {
    const n = document.createElement(tag);
    if (cl) n.className = cl;
    if (text !== undefined) n.textContent = text;
    return n;
  }
  function haystack(x) {
    return [x.title_zh, x.title_en, x.description_zh, x.prompt, x.prompt_adaptation, x.prompt_excerpt, x.prompt_reconstruction, x.production_notes, x.pipeline, x.action_kind, x.cell_spec, x.acceptance, (x.tags || []).join(' ')].join(' ').toLowerCase();
  }
  function posterKind(x) {
    if (x.image26_status === 'failure_sample') return '失败样本 · 不计成功';
    if (x.image26_status === 'not_26') return '2.5 历史规格 · 不是 2.6';
    if (x.media_kind === 'png') return '源站分镜表 PNG · 不是 GIF';
    if (x.media_kind === 'mp4') return '外链 MP4 · 未观看 · 不是 .gif';
    return '仅外链';
  }
  function visibleSet() {
    const search = query.value.trim().toLowerCase();
    const mode = status.value;
    const showHist = history.checked || mode === 'not_26' || mode === 'all';
    const showFail = (failures && failures.checked) || mode === 'failure_sample' || mode === 'all';
    return items.filter((x) => {
      if (x.image26_status === 'not_26' && !showHist && !search) return false;
      if (x.image26_status === 'failure_sample' && !showFail && !search) return false;
      if (mode !== 'default' && mode !== 'all' && x.image26_status !== mode) return false;
      return !search || haystack(x).includes(search);
    });
  }
  function render() {
    const list = visibleSet();
    cards.replaceChildren();
    list.forEach((x, i) => {
      const card = el('article', 'card');
      const poster = el('div', 'poster');
      const candidate = [x.media_url, x.media_poster_url, x.preview].find(approvedMedia);
      if (candidate) {
        const isVideo = /\.(mp4|webm|mov)$/i.test(candidate);
        const preview = el(isVideo ? 'video' : 'img');
        preview.src = candidate;
        if (isVideo) {
          preview.controls = true;
          preview.preload = 'metadata';
        } else {
          preview.alt = x.title_zh;
          preview.loading = 'lazy';
        }
        poster.append(preview);
      } else {
        const source = el(x.source_url ? 'a' : 'div', 'poster-empty', x.source_url ? '查看原始来源 ↗ · 未转载媒体' : '无已获许可预览 · 来源未记录');
        if (x.source_url) {
          source.href = x.source_url;
          source.target = '_blank';
          source.rel = 'noopener noreferrer';
        }
        poster.append(source);
      }
      poster.append(el('span', 'kind', candidate ? posterKind(x) : '仅来源链接 · 未转载媒体'), el('span', 'index', String(i + 1).padStart(2, '0')));
      const content = el('div', 'content');
      content.append(
        el('p', 'game-meta', (statusLabel[x.image26_status] || x.image26_status) + ' · ' + (engineLabel[x.engine_import_status] || '')),
        el('h3', '', x.title_zh),
        el('div', 'en', x.title_en),
        el('p', 'desc', x.description_zh)
      );
      const settings = el('div', 'settings');
      for (const val of [x.model, x.cell_spec, alphaLabel[x.alpha_status] || x.alpha_status, x.media_kind === 'mp4' ? '媒体是 MP4' : '', x.needs_reference_image ? '需要角色参考图' : '', '未复测生成'].filter(Boolean)) {
        settings.append(el('span', '', val));
      }
      content.append(settings);
      if (x.production_notes) content.append(el('p', 'desc', '真实制作要补：' + x.production_notes));
      if (x.prompt_excerpt) content.append(el('p', 'desc', '公开摘录（不是完整 prompt）：' + x.prompt_excerpt));
      content.append(el('p', 'desc', '验收：' + (x.acceptance || '')));
      const audience = {
        game_agent: '给游戏 agent 的原文（不是发给图像模型的 prompt）',
        image_model: x.prompt ? '图像模型原文' : '图像模型原文未公开',
        unpublished: '图像模型原文未公开',
      };
      const promptBox = el('div', x.prompt ? 'prompt' : 'prompt empty');
      const who = el('span', 'who', audience[x.prompt_audience] || (x.prompt ? '第三方原文' : '原文未公开'));
      promptBox.append(who, document.createTextNode('\n' + (x.prompt || '公开来源未给出完整提示词，本站不编造第三方原文。')));
      content.append(promptBox);
      if (x.prompt_reconstruction) {
        const rec = el('div', 'prompt adaptation');
        rec.textContent = '文章重建模板（不是实发原文）：\n' + x.prompt_reconstruction;
        content.append(rec);
      }
      if (x.prompt_adaptation) {
        const adapt = el('div', 'prompt adaptation');
        adapt.textContent = '本站改编（不是第三方原文）：\n' + x.prompt_adaptation;
        content.append(adapt);
      }
      const actions = el('div', 'actions');
      if (x.prompt) {
        const btn = el('button', '', x.prompt_audience === 'game_agent' ? '复制游戏 agent 原文' : '复制原文 Prompt');
        btn.addEventListener('click', async () => {
          try {
            await navigator.clipboard.writeText(x.prompt);
            say('第三方原文已复制');
          } catch {
            say('请手动复制');
          }
        });
        actions.append(btn);
      }
      if (x.prompt_reconstruction) {
        const btn = el('button', '', '复制重建模板');
        btn.addEventListener('click', async () => {
          try {
            await navigator.clipboard.writeText(x.prompt_reconstruction);
            say('重建模板已复制（不是实发原文）');
          } catch {
            say('请手动复制重建框');
          }
        });
        actions.append(btn);
      }
      if (x.prompt_adaptation) {
        const btn = el('button', '', '复制本站改编');
        btn.addEventListener('click', async () => {
          try {
            await navigator.clipboard.writeText(x.prompt_adaptation);
            say('本站改编已复制');
          } catch {
            say('请手动复制改编框');
          }
        });
        actions.append(btn);
      }
      if (x.source_url) {
        const a = el('a', '', '原帖 ↗');
        a.href = x.source_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (approvedMedia(x.media_url)) {
        const a = el('a', '', x.media_kind === 'png' ? '分镜表 PNG ↗' : 'MP4 ↗');
        a.href = x.media_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      (x.related_media_urls || []).filter(approvedMedia).forEach((url, n) => {
        const a = el('a', '', '相关 MP4 ' + (n + 2) + ' ↗');
        a.href = url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      });
      if (approvedMedia(x.media_loop_url)) {
        const a = el('a', '', '切帧循环演示 ↗');
        a.href = x.media_loop_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (x.demo_site_url) {
        const a = el('a', '', '演示站 ↗ 未运行');
        a.href = x.demo_site_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (approvedMedia(x.reference_image_url)) {
        const a = el('a', '', '静图 ↗');
        a.href = x.reference_image_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      (x.related_source_urls || []).slice(0, 4).forEach((url, n) => {
        const a = el('a', '', '相关来源 ' + (n + 1) + ' ↗');
        a.href = url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      });
      content.append(actions);
      card.append(poster, content);
      cards.append(card);
    });
    count.textContent = String(list.length);
    empty.hidden = !!list.length;
  }
  function applyLocation() {
    history.checked = location.hash === '#history';
    if (failures) failures.checked = location.hash === '#fail' || location.hash === '#failures';
    const params = new URLSearchParams(location.search);
    if (params.get('status') && [...status.options].some((o) => o.value === params.get('status'))) {
      status.value = params.get('status');
    }
    render();
  }
  query.addEventListener('input', render);
  status.addEventListener('change', render);
  history.addEventListener('change', render);
  if (failures) failures.addEventListener('change', render);
  window.addEventListener('hashchange', applyLocation);
  applyLocation();
})();
