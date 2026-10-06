// Sampling demo: a sine wave, the points where it is sampled, and the
// simplest wave that fits those samples. Below two samples per cycle the
// fitted wave is slower than the real one, which is aliasing.

const canvas = document.getElementById('signal');
const slider = document.getElementById('rate');
const readout = document.getElementById('rate-value');
const note = document.getElementById('sampler-note');
const ctx = canvas.getContext('2d');

const CYCLES = 6; // cycles of the real wave shown across the canvas

function colour(name) {
  return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
}

function draw() {
  const perCycle = parseFloat(slider.value);
  const w = canvas.width;
  const h = canvas.height;
  const mid = h / 2;
  const amp = h * 0.38;
  const y = (phase) => mid - amp * Math.sin(2 * Math.PI * phase);

  ctx.clearRect(0, 0, w, h);

  // centre line
  ctx.strokeStyle = colour('--rule');
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(0, mid);
  ctx.lineTo(w, mid);
  ctx.stroke();

  // the real wave
  ctx.strokeStyle = colour('--signal');
  ctx.lineWidth = 3;
  ctx.beginPath();
  for (let x = 0; x <= w; x++) {
    const py = y((x / w) * CYCLES);
    if (x === 0) ctx.moveTo(x, py); else ctx.lineTo(x, py);
  }
  ctx.stroke();

  // the wave the samples appear to describe, once sampling is too slow
  const aliased = perCycle < 2;
  if (aliased) {
    const apparent = 1 - perCycle; // cycles of the fitted wave per cycle of the real one
    ctx.strokeStyle = colour('--sample');
    ctx.lineWidth = 2;
    ctx.setLineDash([8, 6]);
    ctx.beginPath();
    for (let x = 0; x <= w; x++) {
      const py = y((x / w) * CYCLES * apparent);
      if (x === 0) ctx.moveTo(x, py); else ctx.lineTo(x, py);
    }
    ctx.stroke();
    ctx.setLineDash([]);
  }

  // the samples
  ctx.fillStyle = colour('--sample');
  ctx.strokeStyle = colour('--sample');
  ctx.lineWidth = 2;
  const total = Math.floor(CYCLES * perCycle);
  for (let n = 0; n <= total; n++) {
    const phase = n / perCycle;
    const x = (phase / CYCLES) * w;
    const py = y(phase);
    ctx.beginPath();
    ctx.moveTo(x, mid);
    ctx.lineTo(x, py);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(x, py, 5, 0, 2 * Math.PI);
    ctx.fill();
  }

  readout.textContent = perCycle.toFixed(1);
  note.textContent = aliased
    ? 'Fewer than two samples per cycle: the samples now fit a slower wave (dashed) just as well as the real one. That is aliasing.'
    : 'More than two samples per cycle, so the samples pin down the wave. Drag left, below 2, to see it break.';
}

slider.addEventListener('input', draw);
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', draw);
new MutationObserver(draw).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
draw();
