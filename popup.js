document.getElementById("sendBtn").addEventListener("click", async () => {
  // Get current tab
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Send URL to Python backend
  const response = await fetch("http://127.0.0.1:5000/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ url: tab.url })
  });

  const data = await response.json();

  document.getElementById("output").innerText = data.result;
});
