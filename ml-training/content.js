// content.js

const API_URL = 'https://ubiquitous-space-goldfish-wr69xxvj46p935r9g-5001.app.github.dev/classify';

function formatPercent(x) {
  // x is between 0 and 1
  return `${Math.round(x * 100)}%`;
}

function createLabel(isHate, confidence) {
  const label = document.createElement('div');
  label.className = 'hate-rating-label-from-extension';

  const status = isHate ? 'HATE' : 'NOT HATE';
  label.textContent = `${status} | Confidence: ${formatPercent(confidence)}`;

  label.style.fontSize = '12px';
  label.style.marginTop = '4px';
  label.style.fontFamily = 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';

  if (isHate) {
    label.style.color = 'red';
  } else {
    label.style.color = 'green';
  }

  return label;
}

async function analyzeTweetElement(tweetTextEl) {
  // Avoid double-processing
  if (tweetTextEl.dataset.hateAnalyzed === 'true') return;
  tweetTextEl.dataset.hateAnalyzed = 'true';

  const text = tweetTextEl.innerText || tweetTextEl.textContent || '';
  if (!text.trim()) return;

  // Small “working” text while the model runs (you can remove this if you hate it)
  const placeholder = document.createElement('div');
  placeholder.textContent = 'Classifying...';
  placeholder.style.fontSize = '12px';
  placeholder.style.color = '#888';
  placeholder.style.marginTop = '4px';
  placeholder.style.fontFamily = 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';
  tweetTextEl.parentElement.appendChild(placeholder);

  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const data = await res.json();
    // Matches your app.py exactly:
    //  data.hate -> boolean
    //  data.confidence -> 0–1 float
    const isHate = Boolean(data.hate);
    const confidence = Number(data.confidence) || 0;

    const label = createLabel(isHate, confidence);
    placeholder.replaceWith(label);
  } catch (err) {
    console.error('Error classifying tweet:', err);
    placeholder.textContent = 'Error classifying';
    placeholder.style.color = 'red';
  }
}

function scanForTweets(root = document) {
  // Twitter/X tweet text container
  const tweetTextEls = root.querySelectorAll('div[data-testid="tweetText"]');
  tweetTextEls.forEach(el => analyzeTweetElement(el));
}

function startObserver() {
  const observer = new MutationObserver(mutations => {
    for (const m of mutations) {
      m.addedNodes.forEach(node => {
        if (!(node instanceof HTMLElement)) return;
        scanForTweets(node);
      });
    }
  });

  observer.observe(document.body, { childList: true, subtree: true });

  // Initial scan
  scanForTweets(document);
}

// Only run on twitter.com / x.com
if (location.hostname.includes('twitter.com') || location.hostname.includes('x.com')) {
  setTimeout(startObserver, 2000);
}