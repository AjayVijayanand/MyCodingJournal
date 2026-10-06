// Phone menu: the Menu button shows and hides the section links.

document.documentElement.classList.add('js');

const nav = document.querySelector('.site-nav');
const toggle = document.querySelector('.menu-toggle');

function setMenu(open) {
  nav.classList.toggle('open', open);
  toggle.setAttribute('aria-expanded', String(open));
}

toggle.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
nav.querySelectorAll('.nav-links a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') setMenu(false);
});

// Photo gallery.
// gallery/photos.json lists every photo with its size (build_gallery.py writes
// it). Photos are laid out in rows that each fill the full width exactly, so
// there are never gaps, whatever mix of tall and wide photos is in the folder.

const section = document.getElementById('gallery');
const link = document.getElementById('gallery-link');
const grid = document.getElementById('gallery-grid');
const more = document.getElementById('gallery-more');

const FIRST = 18;   // photos shown before "Show all" is pressed
const GAP = 10;     // pixels between photos; matches the CSS gap
let tiles = [];
let showAll = false;

function caption(name) {
  return name.replace(/\.[^.]+$/, '').replace(/[-_]+/g, ' ').trim();
}

// Split the visible photos into rows, then size each row to fill the width.
function layout() {
  const width = grid.clientWidth;
  if (!width) return;
  const target = width < 600 ? 150 : 250;   // rough row height in pixels
  const visible = showAll ? tiles : tiles.slice(0, FIRST);
  tiles.forEach((tile) => { tile.el.hidden = !visible.includes(tile); });

  const rows = [];
  let row = [];
  let aspects = 0;
  for (const tile of visible) {
    row.push(tile);
    aspects += tile.aspect;
    if (aspects * target + GAP * (row.length - 1) >= width) {
      rows.push(row);
      row = [];
      aspects = 0;
    }
  }
  if (row.length) {
    // A short last row would leave a gap, so fold it into the row above
    const short = aspects * target + GAP * (row.length - 1) < width * 0.6;
    if (short && rows.length) rows[rows.length - 1].push(...row);
    else rows.push(row);
  }

  for (const r of rows) {
    const total = r.reduce((sum, tile) => sum + tile.aspect, 0);
    const height = (width - GAP * (r.length - 1)) / total;
    for (const tile of r) {
      tile.el.style.width = (tile.aspect * height - 0.05).toFixed(2) + 'px';
      tile.el.style.height = height.toFixed(2) + 'px';
    }
  }
}

function show(photos) {
  tiles = photos.map((photo) => {
    const a = document.createElement('a');
    // photo.src is only set in previews, where the image is embedded in the page
    a.href = photo.src || 'gallery/' + encodeURIComponent(photo.file);
    a.target = '_blank';
    a.rel = 'noopener';
    const img = document.createElement('img');
    img.src = photo.src || 'gallery/thumbs/' + encodeURIComponent(photo.file);
    img.alt = caption(photo.file);
    img.loading = 'lazy';
    img.width = photo.width;
    img.height = photo.height;
    a.append(img);
    grid.append(a);
    return { el: a, aspect: photo.width / photo.height };
  });

  const empty = tiles.length === 0;
  section.hidden = empty;
  link.hidden = empty;
  if (empty) return;

  if (tiles.length > FIRST) {
    more.hidden = false;
    more.textContent = `Show all ${tiles.length} photos`;
    more.addEventListener('click', () => {
      showAll = true;
      more.hidden = true;
      layout();
    });
  }
  layout();
  new ResizeObserver(layout).observe(grid);
}

if (Array.isArray(window.GALLERY_PHOTOS)) {
  // A fixed list, used when previewing the page away from the site
  show(window.GALLERY_PHOTOS);
} else {
  fetch('gallery/photos.json')
    .then((response) => (response.ok ? response.json() : []))
    .then(show)
    .catch(() => show([]));
}
