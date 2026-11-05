(() => {
  'use strict';
  const ideas = Array.isArray(window.GIF_IDEAS) ? window.GIF_IDEAS : [];
  const cards = document.getElementById('cards');
  const query = document.getElementById('search');
  const cat = document.getElementById('category');
  const origin = document.getElementById('origin');
  const count = document.getElementById('visible');
  const empty = document.getElementById('empty');
  const toast = document.getElementById('toast');
  const total = document.getElementById('total');
  if (total) total.textContent = String(ideas.length);

  const statusLabel = {
    verbatim: '逐字公开',
    reconstructed: '本站改写',
    empty: '提示词未公开',
  };
  const kindLabel = {
    gif: 'GIF',
    still: '静图',
    svg: 'SVG',
    edit: '编辑',
    sprite_sheet: 'Sprite',
  };

  for (const c of [...new Set(ideas.map((x) => x.category))]) {
    const o = document.createElement('option');
    o.value = c;
    o.textContent = c;
    cat.append(o);
  }

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
    return [x.title_zh, x.title_en, x.description_zh, (x.tags || []).join(' '), x.prompt, x.output_kind, x.prompt_status]
      .join(' ')
      .toLowerCase();
  }
  function render() {
    const search = query.value.trim().toLowerCase();
    const list = ideas.filter(
      (x) =>
        (cat.value === 'all' || x.category === cat.value) &&
        (origin.value === 'all' || x.origin === origin.value) &&
        haystack(x).includes(search)
    );
    cards.replaceChildren();
    list.forEach((x, i) => {
      const card = el('article', 'card');
      const poster = el('div', 'poster');
      if (x.preview) {
        const img = el('img');
        img.src = x.preview;
        img.alt = (x.preview_kind === 'existing_gif' ? '已有 GIF 预览：' : '原创概念示意图：') + x.title_zh;
        img.loading = 'lazy';
        poster.append(img);
      } else {
        poster.append(el('div', 'poster-empty', '无本地图 · 请打开来源链接'));
      }
      const kindText =
        x.preview_kind === 'existing_gif'
          ? '已有 GIF · 可播放'
          : x.preview_kind === 'link_only'
            ? '仅外链 · 未转载'
            : '原创 SVG · 概念示意';
      poster.append(el('span', 'kind', kindText), el('span', 'index', String(i + 1).padStart(2, '0')));
      const content = el('div', 'content');
      const line = el('div', 'eyeline');
      line.append(el('span', '', x.category + ' · ' + x.source_label), el('span', 'p', x.priority + ' 编辑优先级'));
      content.append(line, el('h3', '', x.title_zh), el('div', 'en', x.title_en), el('p', 'desc', x.description_zh));
      const settings = el('div', 'settings');
      const chips = [x.model, kindLabel[x.output_kind] || x.output_kind, statusLabel[x.prompt_status] || x.prompt_status, x.aspect];
      if (x.frames) chips.splice(1, 0, x.output_kind === 'sprite_sheet' ? x.frames + '格' : x.frames + '帧');
      if (x.frame_duration_ms) chips.push(x.frame_duration_ms + 'ms/帧');
      for (const val of chips) settings.append(el('span', '', val));
      const promptBox = el('div', x.prompt ? 'prompt' : 'prompt empty');
      promptBox.textContent = x.prompt || '公开来源未给出完整提示词，本站不编造第三方原文。';
      content.append(settings, promptBox);
      const actions = el('div', 'actions');
      const btn = el('button', '', x.prompt ? '复制 Prompt' : '无提示词可复制');
      btn.disabled = !x.prompt;
      if (x.prompt) {
        btn.addEventListener('click', async () => {
          try {
            await navigator.clipboard.writeText(x.prompt);
            say('Prompt 已复制');
          } catch {
            const area = document.createElement('textarea');
            area.value = x.prompt;
            document.body.append(area);
            area.select();
            try {
              document.execCommand('copy');
              say('Prompt 已复制');
            } catch {
              say('请手动复制代码框文字');
            }
            area.remove();
          }
        });
      }
      actions.append(btn);
      if (x.source_url) {
        const a = el('a', '', '查看参考 ↗');
        a.href = x.source_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      } else {
        actions.append(el('span', 'disabled', '原创延伸，无外部案例'));
      }
      content.append(actions);
      card.append(poster, content);
      cards.append(card);
    });
    count.textContent = String(list.length);
    empty.hidden = !!list.length;
  }
  query.addEventListener('input', render);
  cat.addEventListener('change', render);
  origin.addEventListener('change', render);
  render();
})();
