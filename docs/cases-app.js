(() => {
  'use strict';
  const catalog = window.COMMUNITY_CASES;
  if (!catalog) return;
  const counts = catalog.meta.counts;
  const publicPaths = new Set(window.PUBLIC_MEDIA_PATHS || []);
  function dict() {
    return window.UI_I18N || {};
  }
  function groups() {
    const g = dict().groups || {};
    const by = catalog.collected_by_family || {};
    const frontier = [
      ...(by.claude || []),
      ...(by.gemini || []),
      ...(by['gpt-code'] || []),
      ...(by.grok || []),
      ...(by.qwen || []),
      ...(by.deepseek || []),
    ];
    return [
      { key: 'main', label: g.main || 'Homepage', rows: frontier },
      { key: 'gpt-image', label: g.gptImage || 'GPT Image', rows: by['gpt-image'] || [] },
      { key: 'x', label: g.x || 'X', rows: catalog.collected_x_author_claim },
      { key: 'web', label: g.web || 'GIF', rows: catalog.collected_web_gif },
      { key: 'inrepo', label: g.inrepo || 'In-repo', rows: catalog.collected_already_in_repo },
      { key: 'game', label: g.game || 'Game', rows: catalog.collected_game_author_claim },
      { key: 'claude', label: g.claude || 'Claude', rows: by.claude || [] },
      { key: 'gemini', label: g.gemini || 'Gemini', rows: by.gemini || [] },
      { key: 'gpt-code', label: g.gptCode || 'GPT Sol', rows: by['gpt-code'] || [] },
      { key: 'grok', label: g.grok || 'Grok', rows: by.grok || [] },
      { key: 'qwen', label: g.qwen || 'Qwen', rows: by.qwen || [] },
      { key: 'deepseek', label: g.deepseek || 'DeepSeek', rows: by.deepseek || [] },
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
  setText('count-x', counts.family_claude);
  setText('count-web', counts.family_gemini);
  setText('count-game', counts['family_gpt-code']);
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
  function link(url, label, local) {
    if (local) return `<a href="${esc(url)}">${esc(label)}</a>`;
    if (!url) return '—';
    return `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`;
  }
  function localized(r, field) {
    const lang = window.UI_LANG === 'zh' ? 'zh-CN' : (window.UI_LANG || 'en');
    return r.translations && r.translations[lang] && r.translations[lang][field] || r[field] || '';
  }
  function translationPage(r) {
    return 'translated-case.html?id=' + encodeURIComponent(r.id) + '&lang=' + encodeURIComponent(window.UI_LANG === 'zh' ? 'zh-CN' : (window.UI_LANG || 'en'));
  }
  function promptLabel(r, d) {
    const status = r.prompt_status || '';
    if (status === 'source_only') return d.promptAtSource || 'Published at source';
    if (status === 'aggregator_only') return d.promptAggregator || 'Aggregator only';
    if (status === 'reconstructed') return window.UI_LANG === 'zh' ? '重建提示词' : 'Reconstructed';
    if (status === '有面向 2.6 的提示词') return window.UI_LANG === 'zh' ? '面向 2.6 的提示词' : 'Prompt targeting 2.6';
    if (status === '空') return d.promptUnpublished || 'Unpublished';
    if (status === '短/部分') return d.promptPartial || 'Short / partial';
    if (status.startsWith('有原文')) return d.promptOriginal || 'Original';
    return status || d.promptFull || 'prompt';
  }
  function promptCell(r, d) {
    const label = promptLabel(r, d);
    if (r.translations && r.original_prompt) return link(translationPage(r) + '#case-prompt', label + ' · ' + (d.translation || 'translation'), true);
    if (r.local_prompt) return link(r.local_prompt.replace(/^docs\//, ''), label, true);
    if (r.prompt_url) return link(r.prompt_url, label);
    return esc(label);
  }
  function mediaCell(r, d) {
    const files = Array.isArray(r.local_files) ? r.local_files.filter((f) => f.public_allowed === true && publicPaths.has((f.path || '').replace(/^docs\//, '')) && /^docs\/(?:cases|assets)\//.test(f.path || '') && !f.path.includes('..')) : [];
    const first = files.find((f) => f.ext === 'gif') || files.find((f) => ['png', 'jpg', 'jpeg', 'webp'].includes(f.ext)) || files.find((f) => f.ext === 'mp4');
    const page = r.local_page || (r.local_dir ? r.local_dir + 'index.html' : '');
    const prompt = r.local_prompt || '';
    let preview = '';
    if (first && first.path) {
      const rel = first.path.replace(/^docs\//, '');
      if (first.ext === 'mp4') {
        preview = `<video src="${esc(rel)}" controls muted loop playsinline preload="metadata" style="max-width:160px;max-height:110px"></video>`;
      } else {
        preview = `<img src="${esc(rel)}" alt="${esc(r.id)}" loading="lazy" style="max-width:160px;max-height:110px;object-fit:contain">`;
      }
    }
    const bits = [preview];
    if (page) bits.push(link(page.replace(/^docs\//, ''), d.local || 'local', true));
    if (prompt) bits.push(promptCell(r, d));
    if (r.source_url) bits.push(link(r.source_url, d.cite || 'source'));
    return bits.filter(Boolean).join('<br>') || '—';
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
      return [r.id, r.author, r.title, r.play, r.model_claim, r.pipeline, r.verify, ...Object.values(r.translations || {}).flatMap(t => [t.title, t.pipeline, t.verify, t.model_claim])]
        .join(' ')
        .toLowerCase()
        .includes(q);
    });
    if (visible) visible.textContent = String(rows.length);
    if (empty) empty.hidden = rows.length > 0;
    if (!tbody) return;
    tbody.innerHTML = rows.map((r, i) => `<tr>
      <td data-label="#">${i + 1}</td>
      <td data-label="${esc(d.thAuthor || 'Author')}">${esc(r.author)}</td>
      <td data-label="${esc(d.thPlay || 'Case')}"><div class="case-title">${r.translations ? link(translationPage(r), localized(r, 'title'), true) : esc(r.title)}</div><div class="case-id">${esc(r.id)}</div></td>
      <td data-label="${esc(d.thPost || 'Source')}">${link(r.source_url, d.post || 'source')}</td>
      <td data-label="${esc(d.thMedia || 'Media')}">${mediaCell(r, d)}</td>
      <td data-label="${esc(d.thPrompt || 'Prompt')}">${promptCell(r, d)}</td>
      <td data-label="${esc(d.thModel || 'Model')}">${esc(localized(r, 'model_claim'))}</td>
      <td data-label="${esc(d.thPipe || 'Pipeline')}">${esc(localized(r, 'pipeline'))}</td>
      <td data-label="${esc(d.thVerify || 'Verification')}">${esc(localized(r, 'verify'))}</td>
      <td data-label="${esc(d.thLicense || 'License')}">${r.license_label && r.license_url ? link(r.license_url, r.license_label) : esc(d.licenseUnknown || 'license unknown')}</td>
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
