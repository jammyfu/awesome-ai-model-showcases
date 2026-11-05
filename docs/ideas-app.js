(() => {
  'use strict';
  const ideas = Array.isArray(window.GIF_IDEAS) ? window.GIF_IDEAS : [];
  const cards = document.getElementById('cards');
  const query = document.getElementById('search');
  const cat = document.getElementById('category');
  const origin = document.getElementById('origin');
  const media = document.getElementById('media');
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
    return [
      x.title_zh,
      x.title_en,
      x.description_zh,
      (x.tags || []).join(' '),
      x.prompt,
      x.output_kind,
      x.prompt_status,
      x.media_kind,
      x.source_label,
      x.example_run_model,
    ]
      .join(' ')
      .toLowerCase();
  }
  function posterKind(x) {
    if (x.preview_kind === 'existing_gif') return '仓库 GIF · 可播放';
    if (x.preview_kind === 'external_gif') return '源站 GIF · 外链播放';
    if (x.media_kind === 'mp4') return 'X 标 GIF · 实际 MP4 · 未观看';
    if (x.demo_kind === 'vimeo') return '官方演示是视频 · 不是 GIF';
    if (x.example_is_image26 === false) return '原创 SVG · 示例不是 2.6';
    if (x.preview_kind === 'link_only') return '仅外链 · 未转载';
    return '原创 SVG · 概念示意';
  }
  function matchesMedia(x) {
    const mode = media ? media.value : 'all';
    if (mode === 'all') return true;
    if (mode === 'playable26') {
      return x.preview_kind === 'existing_gif' || x.preview_kind === 'external_gif';
    }
    if (mode === 'xmp4') return x.media_kind === 'mp4';
    if (mode === 'not26') return x.example_is_image26 === false;
    if (mode === 'svg') return x.preview_kind === 'concept_illustration';
    return true;
  }
  function render() {
    const search = query.value.trim().toLowerCase();
    const list = ideas.filter(
      (x) =>
        (cat.value === 'all' || x.category === cat.value) &&
        (origin.value === 'all' || x.origin === origin.value) &&
        matchesMedia(x) &&
        haystack(x).includes(search)
    );
    cards.replaceChildren();
    list.forEach((x, i) => {
      const card = el('article', 'card');
      const poster = el('div', 'poster');
      if (x.preview_kind === 'external_gif' && x.media_url) {
        const img = el('img');
        img.src = x.media_url;
        img.alt = '源站 GIF（未入库）：' + x.title_zh;
        img.loading = 'lazy';
        img.referrerPolicy = 'no-referrer';
        poster.append(img);
      } else if (x.media_kind === 'mp4' && x.media_poster_url) {
        const img = el('img');
        img.src = x.media_poster_url;
        img.alt = 'X 静帧预览，动图是未观看的 MP4：' + x.title_zh;
        img.loading = 'lazy';
        img.referrerPolicy = 'no-referrer';
        poster.append(img);
      } else if (x.media_kind === 'mp4') {
        poster.append(el('div', 'poster-empty', 'X 标成 GIF · 实际 MP4 · 未视觉复核'));
      } else if (x.preview) {
        const img = el('img');
        img.src = x.preview;
        img.alt =
          (x.preview_kind === 'existing_gif' ? '仓库 GIF 预览：' : '原创概念示意图，不是模型成品：') +
          x.title_zh;
        img.loading = 'lazy';
        poster.append(img);
      } else {
        poster.append(el('div', 'poster-empty', '无本地图 · 请打开来源链接'));
      }
      poster.append(el('span', 'kind', posterKind(x)), el('span', 'index', String(i + 1).padStart(2, '0')));
      const content = el('div', 'content');
      const line = el('div', 'eyeline');
      line.append(el('span', '', x.category + ' · ' + x.source_label), el('span', 'p', x.priority + ' 编辑优先级'));
      content.append(line, el('h3', '', x.title_zh), el('div', 'en', x.title_en), el('p', 'desc', x.description_zh));
      const settings = el('div', 'settings');
      const chips = [x.model, kindLabel[x.output_kind] || x.output_kind, statusLabel[x.prompt_status] || x.prompt_status, x.aspect];
      if (x.frames) chips.splice(1, 0, x.output_kind === 'sprite_sheet' ? x.frames + '格' : x.frames + '帧');
      if (x.frame_duration_ms) chips.push(x.frame_duration_ms + 'ms/帧');
      if (x.example_is_image26 === false) chips.push('示例非 2.6');
      if (x.media_kind && x.media_kind !== 'gif' && x.output_kind === 'gif') chips.push('媒体是 ' + x.media_kind.toUpperCase());
      if (x.author_model_claim_status === 'author_explicit') chips.push('作者声明 2.6');
      if (x.media_metadata_status === 'x_api_and_head_checked') chips.push('媒体元数据已核');
      if (x.visual_review_status === 'unwatched') chips.push('未视觉复核');
      if (x.generation_verified === false) chips.push('未复测生成');
      if (x.frames_basis === 'author_prompt_spec') chips.push('帧数来自提示词规格');
      if (x.frames_basis === 'editorial_recommendation') chips.push('帧数是玩法建议');
      if (x.example_run_model) chips.push(x.example_run_model);
      for (const val of chips) settings.append(el('span', '', val));
      const promptBox = el('div', x.prompt ? 'prompt' : 'prompt empty');
      promptBox.textContent = x.prompt || '公开来源未给出完整提示词，本站不编造第三方原文。';
      content.append(settings, promptBox);
      if (x.prompt_adaptation) {
        const adapt = el('div', 'prompt adaptation');
        adapt.textContent = '本站改编（不是第三方原文）：\n' + x.prompt_adaptation;
        content.append(adapt);
      }
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
      if (x.prompt_adaptation) {
        const adaptBtn = el('button', '', '复制本站改编');
        adaptBtn.addEventListener('click', async () => {
          try {
            await navigator.clipboard.writeText(x.prompt_adaptation);
            say('本站改编已复制');
          } catch {
            say('请手动复制改编框');
          }
        });
        actions.append(adaptBtn);
      }
      if (x.media_url && x.preview_kind === 'external_gif') {
        const a = el('a', '', '源站 GIF ↗');
        a.href = x.media_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (x.media_kind === 'mp4' && x.media_url) {
        const a = el('a', '', 'X MP4 ↗');
        a.href = x.media_url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        actions.append(a);
      }
      if (x.reference_image_url) {
        const a = el('a', '', '参考静图 ↗');
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
  query.addEventListener('input', render);
  cat.addEventListener('change', render);
  origin.addEventListener('change', render);
  if (media) media.addEventListener('change', render);
  render();
})();
