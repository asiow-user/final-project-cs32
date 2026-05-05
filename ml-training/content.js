// content.js

const API_URL = 'https://ubiquitous-space-goldfish-wr69xxvj46p935r9g-5001.app.github.dev/classify';
//link for where the Flask is
function formatPercent(x) {
  // converts into a readable percentage 
  return `${Math.round(x * 100)}%`;
}

function createLabel(isHate, confidence) {
  const label = document.createElement('div');
  label.className = 'hate-rating-label-from-extension';

  // classifys results in a readable way
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
  // avoids double-processing
  if (tweetTextEl.dataset.hateAnalyzed === 'true') return;
  tweetTextEl.dataset.hateAnalyzed = 'true';
//extracts text from a tweet
  const text = tweetTextEl.innerText || tweetTextEl.textContent || '';
  if (!text.trim()) return;

  // placeholder so the user knows what is happening
  const placeholder = document.createElement('div');
  placeholder.textContent = 'Classifying...';
  placeholder.style.fontSize = '12px';
  placeholder.style.color = '#888';
  placeholder.style.marginTop = '4px';
  placeholder.style.fontFamily = 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';
  tweetTextEl.parentElement.appendChild(placeholder);

  try { // send text to backend for classification in the format flask expects
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    // identify that error is happening, and go catch the block
    const data = await res.json();
    // Matches your app.py exactly:
    //  data.hate -> boolean
    //  data.confidence -> 0–1 float
    const isHate = Boolean(data.hate);
    const confidence = Number(data.confidence) || 0;
    // replaces the classifying placeholder with the label 
    const label = createLabel(isHate, confidence);
    placeholder.replaceWith(label);
  } catch (err) {
    console.error('Error classifying tweet:', err);
    placeholder.textContent = 'Error classifying';
    placeholder.style.color = 'red';
  } // handles errors
}

function scanForTweets(root = document) {
  // finds all the tweet text containers on the page and then analyzes them
  const tweetTextEls = root.querySelectorAll('div[data-testid="tweetText"]');
  tweetTextEls.forEach(el => analyzeTweetElement(el));
}

function startObserver() { //content loads without page refresh so checks if new content loads
  const observer = new MutationObserver(mutations => {
    for (const m of mutations) {
      m.addedNodes.forEach(node => {
        if (!(node instanceof HTMLElement)) return;
        scanForTweets(node);
      });
    }
  });

  observer.observe(document.body, { childList: true, subtree: true });

  // initial scan
  scanForTweets(document);
}

// only run on twitter.com / x.com
if (location.hostname.includes('twitter.com') || location.hostname.includes('x.com')) {
  setTimeout(startObserver, 2000);
}