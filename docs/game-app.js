(() => {
  'use strict';
  const all = Array.isArray(window.GIF_IDEAS) ? window.GIF_IDEAS : [];
  const items = all.filter((x) => x.game_sequence);
  const cards = document.getElementById('cards');
  const query = document.getElementById('search');
  const status = document.getElementById('status');
  const history = document.getElementById('history');
  const count = document.getElementById('visible');
  const empty = document.getElementById('empty');
  const toast = document.getElementById('toast');
  const authorN = items.filter((x) => (x.tags || []).includes('x-original-author')).length;
  const multiN = items.filter((x) => x.image26_status === 'multimodel_postprocess').length;
  const promoN = items.filter((x) => x.image26_status === 'promo_claim_unwatched').length;
  const elA = document.getElementById('authorN');
  const elM = document.getElementById('multiN');
  const elP = document.getElementById('promoN');
  if (elA) elA.textContent = String(authorN);
  if (elM) elM.textContent = String(multiN);
  if (elP) elP.textContent = String(promoN);
  const statusLabel = {
    author_claim_unverified: '原作者声明 2.6 · 非官方验证',
    multimodel_postprocess: '含其他模型后处理 · 不是纯 2.6',
    promo_claim_unwatched: '宣传方宣称 · 未观看',
    not_26: 'GPT Image 2.5 · 不是 2.6',
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
    return [x.title_zh, x.title_en, x.description_zh, x.prompt, x.prompt_adaptation, x.prompt_excerpt, x.pipeline, x.action_kind, x.cell_spec, x.acceptance, (x.tags || []).join(' ')].join(' ').toLowerCase();
  }
  function posterKind(x) {
    if (x.image26_status === 'not_26') return '2.5 历史规格 · 不是 2.6';
    if (x.media_kind === 'png') return '源站分镜表 PNG · 不是 GIF';
    if (x.media_kind === 'mp4') return '外链 MP4 · 未观看 · 不是 .gif';
    return '仅外链';
  }
  function visibleSet() {
    const search = query.value.trim().toLowerCase();
    const mode = status.value;
    const showHist = history.checked || mode === 'not_26' || mode === 'all';
    return items.filter((x) => {
      if (x.default_hidden && !showHist && !search) return false;
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
      if (x.media_kind === 'png' && x.media_url) {
        const img = el('img');
        img.src = x.media_url;
        img.alt = '源站 Sprite 表（静图，未入库）：' + x.title_zh;
        img.loading = 'lazy';
        img.referrerPolicy = 'no-referrer';
        poster.append(img);
      } else if (x.media_poster_url) {
        const img = el('img');
        img.src = x.media_poster_url;
        img.alt = '静帧预览，动媒是未观看的 MP4：' + x.title_zh;
        img.loading = 'lazy';
        img.referrerPolicy = 'no-referrer';
        poster.append(img);
      } else {
        poster.append(el('div', 'poster-empty', '打开来源查看 MP4 / 分镜 · 不是 SVG 成品'));
      }
      poster.append(el('span', 'kind', posterKind(x)), el('span', 'index', String(i + 1).padStart(2, '0')));
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
      if (x.prompt_excerpt) content.append(el('p', 'desc', '公开摘录（不是完整 prompt）：' + x.prompt_excerpt));
      content.append(el('p', 'desc', '验收：' + (x.acceptance || '')));
      const promptBox = el('div', x.prompt ? 'prompt' : 'prompt empty');
      promptBox.textContent = x.prompt || '公开来源未给出完整提示词，本站不编造第三方原文。';
      content.append(promptBox);
      if (x.prompt_adaptation) {
        const adapt = el('div', 'prompt adaptation');
        adapt.textContent = '本站改编（不是第三方原文）：\n' + x.prompt_adaptation;
        content.append(adapt);
      }
      const actions = el('div', 'actions');
      if (x.prompt) {
        const btn = el('button', '', '复制原文 Prompt');
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
      if (x.media_url) {
        const a = el('a', '', x.media_kind === 'png' ? '分镜表 PNG ↗' : 'MP4 ↗');
        a.href = x.media_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      (x.related_media_urls || []).forEach((url, n) => {
        const a = el('a', '', '相关 MP4 ' + (n + 2) + ' ↗');
        a.href = url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      });
      if (x.media_loop_url) {
        const a = el('a', '', '切帧循环演示 ↗');
        a.href = x.media_loop_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (x.reference_image_url) {
        const a = el('a', '', '静图 ↗');
        a.href = x.reference_image_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      content.append(actions);
      card.append(poster, content);
      cards.append(card);
    });
    count.textContent = String(list.length);
    empty.hidden = !!list.length;
  }
  function applyLocation() {
    history.checked = location.hash === '#history';
    const params = new URLSearchParams(location.search);
    if (params.get('status') && [...status.options].some((o) => o.value === params.get('status'))) {
      status.value = params.get('status');
    }
    render();
  }
  query.addEventListener('input', render);
  status.addEventListener('change', render);
  history.addEventListener('change', render);
  window.addEventListener('hashchange', applyLocation);
  applyLocation();
})();
