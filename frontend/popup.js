const urlElement = document.getElementById("url");
const resultDiv = document.getElementById("result");

chrome.tabs.query({ active: true, currentWindow: true }, async (tabs) => {
  if (!tabs.length || !tabs[0].url) {
    urlElement.textContent = "❌ No active tab URL found.";
    resultDiv.innerHTML = "<p>Cannot summarize this page.</p>";
    return;
  }

  const pageUrl = tabs[0].url;
  urlElement.textContent = pageUrl;

  try {
    const apiUrl =
      `http://localhost:8000/url?url=${encodeURIComponent(pageUrl)}`;

    const response = await fetch(apiUrl);
    const summary = await response.json();

    resultDiv.innerHTML = `<p>${summary}</p>`;
  } catch (err) {
    console.error(err);
    resultDiv.innerHTML = "<p>❌ Failed to load summary</p>";
  }
});
