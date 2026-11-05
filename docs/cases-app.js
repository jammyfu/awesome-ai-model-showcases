(() => {
  'use strict';
  const catalog = window.COMMUNITY_CASES;
  if (!catalog) return;
  const counts = catalog.meta.counts;
  function dict() {
    return window.UI_I18N || {};
  }
  function groups() {
    const g = dict().groups || {};
    return [
      { key: 'main', label: g.main || 'Collected', rows: [
        ...catalog.collected_x_author_claim,
        ...catalog.collected_web_gif,
        ...catalog.collected_already_in_repo,
        ...catalog.collected_game_author_claim,
      ] },
      { key: 'x', label: g.x || 'X', rows: catalog.collected_x_author_claim },
      { key: 'web', label: g.web || 'GIF', rows: catalog.collected_web_gif },
      { key: 'inrepo', label: g.inrepo || 'In-repo', rows: catalog.collected_already_in_repo },
      { key: 'game', label: g.game || 'Game', rows: catalog.collected_game_author_claim },
      { key: 'pending', label: g.pending || 'Pending', rows: catalog.pending },
      { key: 'appendix', label: g.appendix || 'Appendix', rows: [...catalog.prompt_only, ...catalog.excluded, ...catalog.appendix] },
      { key: 'seeds', label: g.seeds || 'Seeds', rows: catalog.repo_seeds },
    ];
  }

  const setText = (id, value) => {
    const el = document.getElementById(id);
    if (el) el.textContent = String(value);
  };
  setText('count-main', counts.main_collected);
  setText('count-x', counts.x_author_claim_25);
  setText('count-web', counts.web_gif_12);
  setText('count-game', counts.game_author_claim);
  setText('count-pending', counts.pending);
  setText('count-appendix', counts.appendix);

  const tbody = document.getElementById('case-rows');
  const visible = document.getElementById('case-visible');
  const empty = document.getElementById('case-empty');
  const search = document.getElementById('case-search');
  const chips = document.getElementById('case-filters');
  let bucket = 'main';

  function esc(s) {
    return String(s || '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  }
  function link(url, label) {
    if (!url) return '—';
    return `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`;
  }
  function renderChips() {
    if (!chips) return;
    chips.replaceChildren();
    groups().forEach((g) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'chip' + (g.key === bucket ? ' active' : '');
      b.textContent = `${g.label} ${g.rows.length}`;
      b.addEventListener('click', () => {
        bucket = g.key;
        renderChips();
        render();
      });
      chips.append(b);
    });
  }
  function render() {
    const d = dict();
    const q = (search && search.value || '').trim().toLowerCase();
    const list = groups();
    const group = list.find((g) => g.key === bucket) || list[0];
    const rows = group.rows.filter((r) => {
      if (!q) return true;
      return [r.id, r.author, r.title, r.play, r.model_claim, r.pipeline, r.verify]
        .join(' ')
        .toLowerCase()
        .includes(q);
    });
    if (visible) visible.textContent = String(rows.length);
    if (empty) empty.hidden = rows.length > 0;
    if (!tbody) return;
    tbody.innerHTML = rows.map((r, i) => `<tr>
      <td>${i + 1}</td>
      <td>${esc(r.author)}</td>
      <td><div class="case-title">${esc(r.title)}</div><div class="case-id">${esc(r.id)}</div></td>
      <td>${link(r.source_url, d.post || 'post')}</td>
      <td>${link(r.media_url, r.media_kind || 'media')}</td>
      <td>${esc(r.prompt_status)}</td>
      <td>${esc((r.model_claim || '').slice(0, 48))}</td>
      <td>${esc(r.pipeline)}</td>
      <td>${esc(r.verify)}</td>
      <td>${esc(d.linkOnly || 'link-only')}</td>
    </tr>`).join('');
  }
  if (search) search.addEventListener('input', render);
  document.addEventListener('ui-lang', () => {
    renderChips();
    render();
  });
  function start() {
    renderChips();
    render();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
