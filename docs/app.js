(() => {
  'use strict';
  const data = Array.isArray(window.GALLERY_ITEMS) ? window.GALLERY_ITEMS : [];
  const cards = document.getElementById('cards');
  const filters = document.getElementById('filters');
  const input = document.getElementById('search');
  const visible = document.getElementById('visible-count');
  const empty = document.getElementById('empty');
  const toast = document.getElementById('toast');
  let category = 'All';
  let storage = 'All';
  let toastTimer;
  const gifs = data.filter((item) => (item.media_kind || 'gif') === 'gif');
  const localCount = gifs.filter((item) => (item.storage || 'local') === 'local').length;
  const sourceCount = gifs.filter((item) => item.storage === 'external').length;
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
    ['All', 'Local', 'Source GIF'].forEach((item) => {
      const button = node('button', 'chip storage' + (item === storage ? ' active' : ''), item);
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
    const isExternal = item.storage === 'external';
    const card = node('article', 'card');
    const preview = node('a', 'preview');
    preview.href = item.image;
    preview.target = '_blank';
    preview.rel = 'noopener noreferrer';
    preview.setAttribute('aria-label', 'Open ' + item.title + (isExternal ? ' source GIF' : ' animated GIF'));
    const image = node('img');
    image.src = item.image;
    image.alt = item.description;
    image.loading = 'lazy';
    image.decoding = 'async';
    if (isExternal) image.referrerPolicy = 'no-referrer';
    const pill = node('span', 'pill', (isExternal ? 'SOURCE GIF' : 'LOCAL') + ' · ' + item.category.toUpperCase());
    preview.append(image, pill);
    const content = node('div', 'card-content');
    const h3 = node('h3', '', item.title);
    const description = node('p', '', item.description);
    const tags = node('div', 'tags');
    item.tags.forEach((tag) => tags.append(node('span', 'tag', '#' + tag)));
    const bottom = node('div', 'card-bottom');
    const meta = node(
      'span',
      'card-meta',
      item.frames + ' frames · ' + (item.duration_ms / 1000).toFixed(2) + 's' + (isExternal ? ' · link-only' : '')
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
        (storage === 'Local' && (item.storage || 'local') === 'local') ||
        (storage === 'Source GIF' && item.storage === 'external');
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
  renderFilters();
  render();
})();
