// Photo gallery.
// Every image in the gallery/ folder is shown automatically: the list of files
// is read from GitHub, so adding a photo to that folder and pushing is all it
// takes. The caption comes from the file name.

const OWNER = 'AjayVijayanand';
const REPO = 'MyCodingJournal';
const FOLDER = 'PortfolioWebsite/gallery';

const section = document.getElementById('gallery');
const link = document.getElementById('gallery-link');
const grid = document.getElementById('gallery-grid');

const isImage = (name) => /\.(jpe?g|png|webp|gif|avif)$/i.test(name);

function caption(name) {
  return name.replace(/\.[^.]+$/, '').replace(/[-_]+/g, ' ').trim();
}

function show(names) {
  const photos = names.filter(isImage).sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
  for (const name of photos) {
    const a = document.createElement('a');
    a.href = 'gallery/' + encodeURIComponent(name);
    a.target = '_blank';
    a.rel = 'noopener';
    const img = document.createElement('img');
    img.src = a.href;
    img.alt = caption(name);
    img.loading = 'lazy';
    a.append(img);
    grid.append(a);
  }
  const empty = photos.length === 0;
  section.hidden = empty;
  link.hidden = empty;
}

if (Array.isArray(window.GALLERY_FILES)) {
  // A fixed list, used when previewing the page away from GitHub
  show(window.GALLERY_FILES);
} else {
  fetch(`https://api.github.com/repos/${OWNER}/${REPO}/contents/${FOLDER}?ref=main`)
    .then((response) => (response.ok ? response.json() : []))
    .then((files) => show(files.filter((f) => f.type === 'file').map((f) => f.name)))
    .catch(() => show([]));
}
