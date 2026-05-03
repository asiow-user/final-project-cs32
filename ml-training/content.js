async function classifyText(text) {
  const response = await fetch("http://localhost:5000/classify", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text })
  });

  return response.json();
}

async function processTweet(tweetElement) {
  const text = tweetElement.innerText;

  if (!text) return;

  const result = await classifyText(text);

  if (result.hate && result.confidence > 0.8) {
    tweetElement.style.filter = "blur(6px)";
    tweetElement.title = "Flagged as hate speech (click to reveal)";

    tweetElement.addEventListener("click", () => {
      tweetElement.style.filter = "none";
    });
  }
}

// Watch for tweets dynamically
const observer = new MutationObserver(() => {
  const tweets = document.querySelectorAll('[data-testid="tweetText"]');

  tweets.forEach(tweet => {
    if (!tweet.dataset.checked) {
      tweet.dataset.checked = "true";
      processTweet(tweet);
    }
  });
});

observer.observe(document.body, { childList: true, subtree: true });
