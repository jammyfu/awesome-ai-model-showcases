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
  let toastTimer;
  const categories = ['All', ...new Set(data.map(item => item.category))];
  document.getElementById('gif-count').textContent = String(data.length);
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
    categories.forEach(item => {
      const button = node('button','chip' + (item === category ? ' active' : ''),item);
      button.type = 'button';
      button.setAttribute('aria-pressed',String(item === category));
      button.addEventListener('click',() => { category = item; renderFilters(); render(); });
      filters.append(button);
    });
  }
  function createCard(item) {
    const card = node('article','card');
    const preview = node('a','preview');
    preview.href = item.image;
    preview.target = '_blank';
    preview.rel = 'noopener noreferrer';
    preview.setAttribute('aria-label','Open ' + item.title + ' animated GIF');
    const image = node('img');
    image.src = item.image; image.alt = item.description;
    image.loading = 'lazy';
    image.decoding = 'async';
    const pill = node('span','pill',item.category.toUpperCase());
    preview.append(image,pill);
    const content = node('div','card-content');
    const h3 = node('h3','',item.title);
    const description = node('p','',item.description);
    const tags = node('div','tags');
    item.tags.forEach(tag => tags.append(node('span','tag','#' + tag)));
    const bottom = node('div','card-bottom');
    const meta = node('span','card-meta',item.frames + ' frames · ' + (item.duration_ms/1000).toFixed(2) + 's');
    const copy = node('button','copy','Copy prompt ↗');
    copy.type = 'button'; copy.setAttribute('aria-label','Copy prompt for ' + item.title);
    copy.addEventListener('click', async () => {
      try {
        if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(item.prompt);
        else {
          const area = document.createElement('textarea');
          area.value = item.prompt;area.style.position='fixed';area.style.left='-9999px';
          document.body.append(area);area.select();
          if (!document.execCommand('copy')) throw new Error('Copy unavailable');
          area.remove();
        }
        message('Prompt copied!');
      } catch { message('Copy failed. See prompts/ in the repository.'); }
    });
    bottom.append(meta,copy);
    content.append(h3,description,tags,bottom);
    card.append(preview,content);
    return card;
  }
  function render() {
    const query = input.value.trim().toLowerCase();
    const filtered = data.filter(item =>
      (category === 'All' || item.category === category) &&
      (item.title + ' ' + item.description + ' ' + item.description_zh + ' ' + item.tags.join(' ')).toLowerCase().includes(query)
    );
    cards.replaceChildren(...filtered.map(createCard));
    visible.textContent = String(filtered.length).padStart(2,'0');
    empty.hidden = filtered.length !== 0;
  }
  input.addEventListener('input',render);
  window.addEventListener('keydown',event => {
    const active = document.activeElement;
    if (event.key === '/' && active !== input && !['INPUT','TEXTAREA'].includes(active.tagName)) {
      event.preventDefault();input.focus();
    }
    if (event.key === 'Escape' && active === input) {input.value = '';input.blur();render();}
  });
  renderFilters();render();
})();
