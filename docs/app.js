(() => {
  'use strict';
  // Fail closed: only exact docs-relative paths from the verified build registry.
  const publicMedia = new Set(Array.isArray(window.PUBLIC_MEDIA_PATHS) ? window.PUBLIC_MEDIA_PATHS : []);
  function approvedMedia(path) {
    return typeof path === 'string' && !/[:?#\\]/.test(path) && !path.startsWith('/') &&
      !path.split('/').some((part) => !part || part === '.' || part === '..') && publicMedia.has(path);
  }
  const data = Array.isArray(window.GALLERY_ITEMS) ? window.GALLERY_ITEMS : [];
  const cards = document.getElementById('cards');
  const filters = document.getElementById('filters');
  const input = document.getElementById('search');
  const visible = document.getElementById('visible-count');
  const empty = document.getElementById('empty');
  const toast = document.getElementById('toast');
  let category = 'All';
  let storage = 'Source GIF';
  let toastTimer;
  const gifs = data.filter((item) => (item.media_kind || 'gif') === 'gif');
  const localCount = gifs.filter((item) => item.rights === 'repo_seed').length;
  const sourceCount = gifs.filter((item) => item.rights === 'unknown_archived' || item.storage === 'external').length;
  const gifCount = document.getElementById('gif-count');
  if (gifCount) gifCount.textContent = String(gifs.length);
  const localEl = document.getElementById('local-count');
  if (localEl) localEl.textContent = String(localCount);
  const sourceEl = document.getElementById('source-count');
  if (sourceEl) sourceEl.textContent = String(sourceCount);
  const categories = ['All', ...new Set(gifs.map((item) => item.category))];
  function node(tag, className, content) {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (content != null) element.textContent = String(content);
    return element;
  }
  function message(text) {
    toast.textContent = text;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 1800);
  }
  function renderFilters() {
    filters.replaceChildren();
    categories.forEach((item) => {
      const button = node('button', 'chip' + (item === category ? ' active' : ''), item);
      button.type = 'button';
      button.setAttribute('aria-pressed', String(item === category));
      button.addEventListener('click', () => {
        category = item;
        renderFilters();
        render();
      });
      filters.append(button);
    });
    const storageLabels = (window.UI_LANG === 'zh')
      ? { All: '全部', Local: '本地种子', 'Source GIF': '源站 GIF' }
      : { All: 'All', Local: 'Local', 'Source GIF': 'Source GIF' };
    ['All', 'Local', 'Source GIF'].forEach((item) => {
      const button = node('button', 'chip storage' + (item === storage ? ' active' : ''), storageLabels[item]);
      button.type = 'button';
      button.setAttribute('aria-pressed', String(item === storage));
      button.addEventListener('click', () => {
        storage = item;
        renderFilters();
        render();
      });
      filters.append(button);
    });
  }
  function createCard(item) {
    const isExternal = item.storage === 'external' && item.rights !== 'unknown_archived';
    const isArchived = item.rights === 'unknown_archived';
    const card = node('article', 'card');
    const allowed = approvedMedia(item.image);
    const preview = node(allowed || item.source_url ? 'a' : 'div', 'preview');
    if (allowed || item.source_url) {
      preview.href = allowed ? item.image : item.source_url;
      preview.target = '_blank';
      preview.rel = 'noopener noreferrer';
    }
    preview.setAttribute('aria-label', 'Open ' + item.title + ' source');
    if (allowed) {
      const image = node('img');
      image.src = item.image;
      image.alt = item.description;
      image.loading = 'lazy';
      image.decoding = 'async';
      preview.append(image);
    } else {
      preview.append(node('span', 'poster-empty', item.source_url ? 'View original source ↗' : 'Preview unavailable; source not recorded'));
    }
    const pill = node('span', 'pill', (allowed ? 'LICENSED PREVIEW' : 'SOURCE ONLY') + ' · ' + item.category.toUpperCase());
    preview.append(pill);
    const content = node('div', 'card-content');
    const h3 = node('h3', '', item.title);
    const description = node('p', '', item.description);
    const tags = node('div', 'tags');
    item.tags.forEach((tag) => tags.append(node('span', 'tag', '#' + tag)));
    const bottom = node('div', 'card-bottom');
    const meta = node(
      'span',
      'card-meta',
      item.frames + ' frames · ' + (item.duration_ms / 1000).toFixed(2) + 's' + (item.rights === 'unknown_archived' ? ' · local archive' : '')
    );
    const copy = node('button', 'copy', item.prompt ? 'Copy prompt ↗' : 'No prompt');
    copy.type = 'button';
    copy.disabled = !item.prompt;
    copy.setAttribute('aria-label', 'Copy prompt for ' + item.title);
    if (item.prompt) {
      copy.addEventListener('click', async () => {
        try {
          if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(item.prompt);
          else {
            const area = document.createElement('textarea');
            area.value = item.prompt;
            area.style.position = 'fixed';
            area.style.left = '-9999px';
            document.body.append(area);
            area.select();
            if (!document.execCommand('copy')) throw new Error('Copy unavailable');
            area.remove();
          }
          message('Prompt copied!');
        } catch {
          message('Copy failed. See the source page.');
        }
      });
    }
    bottom.append(meta, copy);
    if (item.source_url) {
      const src = node('a', 'source-link', (item.creator || 'Source') + ' ↗');
      src.href = item.source_url;
      src.target = '_blank';
      src.rel = 'noopener noreferrer';
      content.append(h3, description, tags, src, bottom);
    } else {
      content.append(h3, description, tags, bottom);
    }
    card.append(preview, content);
    return card;
  }
  function render() {
    const query = input.value.trim().toLowerCase();
    const filtered = gifs.filter((item) => {
      const storageOk =
        storage === 'All' ||
        (storage === 'Local' && item.rights === 'repo_seed') ||
        (storage === 'Source GIF' && (item.rights === 'unknown_archived' || item.storage === 'external'));
      const hay = (item.title + ' ' + item.description + ' ' + (item.description_zh || '') + ' ' + item.tags.join(' ') + ' ' + (item.creator || '')).toLowerCase();
      return (category === 'All' || item.category === category) && storageOk && hay.includes(query);
    });
    cards.replaceChildren(...filtered.map(createCard));
    visible.textContent = String(filtered.length).padStart(2, '0');
    empty.hidden = filtered.length !== 0;
  }
  input.addEventListener('input', render);
  window.addEventListener('keydown', (event) => {
    const active = document.activeElement;
    if (event.key === '/' && active !== input && !['INPUT', 'TEXTAREA'].includes(active.tagName)) {
      event.preventDefault();
      input.focus();
    }
    if (event.key === 'Escape' && active === input) {
      input.value = '';
      input.blur();
      render();
    }
  });
  document.addEventListener('ui-lang', () => {
    renderFilters();
    render();
  });
  renderFilters();
  render();
})();
