(() => {
  'use strict';
  const all = Array.isArray(window.GIF_IDEAS) ? window.GIF_IDEAS : [];
  const items = all.filter((x) => x.game_sequence);
  const cards = document.getElementById('cards');
  const query = document.getElementById('search');
  const pipe = document.getElementById('pipe');
  const count = document.getElementById('visible');
  const empty = document.getElementById('empty');
  const toast = document.getElementById('toast');
  const total = document.getElementById('total');
  if (total) total.textContent = String(items.length);
  const engineLabel = {
    none: '无引擎导入证据',
    documented_not_run: '有导入步骤 · 作者未实机跑',
    author_claim_unwatched: '作者宣称游戏演示 · 本仓未观看',
  };
  const alphaLabel = {
    solid_white_then_key_not_true_alpha: '白底再抠色 · 不是真 alpha',
    keyed_white_not_true_alpha: '白底抠色 · 不是真 alpha',
    gif_1bit_if_native_gif_unknown_here: '若是原生 GIF 多为 1-bit 透明 · 此处未核',
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
    return [
      x.title_zh,
      x.title_en,
      x.description_zh,
      x.prompt,
      x.prompt_adaptation,
      x.pipeline,
      x.action_kind,
      x.cell_spec,
      x.acceptance,
      (x.tags || []).join(' '),
    ]
      .join(' ')
      .toLowerCase();
  }
  function posterKind(x) {
    if (x.media_kind === 'png') return '源站分镜表 PNG · 不是 GIF';
    if (x.media_kind === 'mp4') return '外链视频/MP4 · 未观看 · 不是 .gif';
    return '仅外链';
  }
  function render() {
    const search = query.value.trim().toLowerCase();
    const list = items.filter(
      (x) =>
        (pipe.value === 'all' || x.pipeline === pipe.value) &&
        haystack(x).includes(search)
    );
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
        img.alt = '静帧预览，动媒未观看：' + x.title_zh;
        img.loading = 'lazy';
        img.referrerPolicy = 'no-referrer';
        poster.append(img);
      } else {
        poster.append(el('div', 'poster-empty', '不是原作 GIF · 打开来源查看分镜或演示'));
      }
      poster.append(el('span', 'kind', posterKind(x)), el('span', 'index', String(i + 1).padStart(2, '0')));
      const content = el('div', 'content');
      content.append(
        el('p', 'game-meta', (x.pipeline || '') + ' · ' + (x.action_kind || '') + ' · ' + (engineLabel[x.engine_import_status] || x.engine_import_status || '')),
        el('h3', '', x.title_zh),
        el('div', 'en', x.title_en),
        el('p', 'desc', x.description_zh)
      );
      const settings = el('div', 'settings');
      for (const val of [
        x.model,
        x.cell_spec,
        alphaLabel[x.alpha_status] || x.alpha_status,
        x.needs_reference_image ? '需要角色参考图' : '未要求参考图',
        x.example_is_image26 === false ? '示例不是 2.6' : '作者声明 2.6',
        '未复测生成',
      ].filter(Boolean)) {
        settings.append(el('span', '', val));
      }
      content.append(settings);
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
        const a = el('a', '', '原帖 / 规格 ↗');
        a.href = x.source_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (x.media_url) {
        const a = el('a', '', x.media_kind === 'png' ? '分镜表 PNG ↗' : '媒体 ↗');
        a.href = x.media_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (x.media_loop_url) {
        const a = el('a', '', '切帧循环演示 ↗');
        a.href = x.media_loop_url;
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
  query.addEventListener('input', render);
  pipe.addEventListener('change', render);
  render();
})();
