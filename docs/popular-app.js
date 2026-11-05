(() => {
  'use strict';
  const pack = window.POPULAR_PLAYBOOKS || {};
  const items = Array.isArray(pack.items) ? pack.items : [];
  const cards = document.getElementById('cards');
  const query = document.getElementById('search');
  const bucket = document.getElementById('bucket');
  const count = document.getElementById('visible');
  const empty = document.getElementById('empty');
  const toast = document.getElementById('toast');
  const total = document.getElementById('total');
  if (total) total.textContent = String(items.length);

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
      x.original_work,
      x.emotion,
      x.everyday_scene,
      x.remake_prompt_zh,
      x.chart,
      x.rank,
      x.chart_bucket,
      x.priority_mechanism,
      x.motion_beats,
      x.sampled_at,
    ]
      .join(' ')
      .toLowerCase();
  }
  function yearLabel(x) {
    return x.year ? String(x.year) : x.year_label || '经典';
  }
  function render() {
    const search = query.value.trim().toLowerCase();
    const list = items.filter(
      (x) =>
        (bucket.value === 'all' || x.chart_bucket === bucket.value) &&
        haystack(x).includes(search)
    );
    cards.replaceChildren();
    list.forEach((x, i) => {
      const card = el('article', 'card');
      const poster = el('div', 'poster');
      poster.append(el('div', 'poster-empty', '不是原作 GIF · 不是 2.6 成品 · 打开原 GIF 页当参考'));
      poster.append(el('span', 'kind', yearLabel(x) + ' · ' + x.chart_bucket), el('span', 'index', String(i + 1).padStart(2, '0')));
      const content = el('div', 'content');
      content.append(
        el('p', 'chart-meta', x.platform + ' · ' + x.rank + (x.sampled_at ? ' · 采样 ' + x.sampled_at : '')),
        el('h3', '', x.title_zh),
        el('div', 'en', x.title_en),
        el('p', 'desc', x.everyday_scene)
      );
      const settings = el('div', 'settings');
      for (const val of [x.platform, x.emotion, '未实测生成', x.metric]) {
        settings.append(el('span', '', val));
      }
      content.append(settings);
      content.append(el('p', 'desc', '原作：' + x.original_work + ' · ' + x.original_author));
      content.append(el('p', 'desc', '节拍：' + x.motion_beats));
      content.append(el('p', 'desc', '逐帧：' + x.frame_plan));
      content.append(el('p', 'desc', '镜头 / 循环：' + x.camera + ' ' + x.loop));
      content.append(el('p', 'desc', '参考图：' + x.need_reference));
      content.append(el('p', 'desc', '验收：' + x.acceptance));
      content.append(el('p', 'desc', '门槛 / 依赖：' + x.demo_barrier + ' ' + x.reproduction_deps));
      const promptBox = el('div', 'prompt adaptation');
      promptBox.textContent = '本项目策划（未实测）：\n' + x.remake_prompt_zh;
      content.append(promptBox);
      const actions = el('div', 'actions');
      const btn = el('button', '', '复制重演 Prompt');
      btn.addEventListener('click', async () => {
        try {
          await navigator.clipboard.writeText(x.remake_prompt_zh);
          say('本仓重演 Prompt 已复制');
        } catch {
          say('请手动复制');
        }
      });
      const chart = el('a', '', '榜单证据 ↗');
      chart.href = x.evidence_url;
      chart.target = '_blank';
      chart.rel = 'noopener noreferrer';
      const gif = el('a', '', '原 GIF 参考 ↗');
      gif.href = x.original_gif_page;
      gif.target = '_blank';
      gif.rel = 'noopener noreferrer';
      actions.append(btn, chart, gif);
      content.append(actions);
      card.append(poster, content);
      cards.append(card);
    });
    count.textContent = String(list.length);
    empty.hidden = !!list.length;
  }
  query.addEventListener('input', render);
  bucket.addEventListener('change', render);
  render();
})();
