# 🌐 Website Summarizer (Chrome Extension + FastAPI)

Website Summarizer is a simple Chrome Extension backed by a FastAPI server that summarizes the content of any website you are currently viewing.
Just open a webpage, click the extension, and get a clean AI-generated summary in seconds.

This project is built mainly for learning and experimentation with **FastAPI, LangChain, and browser extensions**.

---

## Features

* Automatically detects the active browser tab URL
* Summarizes webpage content using an LLM (Mistral 7B Instruct)
* FastAPI backend with in-memory caching
* Simple and clean Chrome Extension UI
* Avoids repeated summarization of the same URL
* Works on most publicly accessible websites

---

##  Project Structure

```
Website-Summarizer/
│
├── backend/
│   ├── main.py
│   ├── pass_url.py
│   ├── summerizer.py
│   └── .env
│
└── frontend/
    ├── manifest.json
    ├── popup.html
    ├── popup.js
    └── style.css
```

---

## Backend Setup (FastAPI)

### Install Dependencies

```bash
pip install fastapi uvicorn python-dotenv langchain langchain-community langchain-huggingface
```

---

### Environment Variables

Create a `.env` file inside the `backend/` directory and add your HuggingFace token:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

### Run the Backend Server

From the `backend/` directory:

```bash
uvicorn main:app --reload
```

The backend will be available at:

```
http://localhost:8000
```

---

## API Endpoint

### **GET** `/url`

Summarizes the given website URL.

* `url` → **(Query Parameter)** Website URL to summarize

**Example**

```
http://localhost:8000/url?url=https://example.com
```

**Response**

```json
"This is a short and clear summary of the webpage content..."
```

---

## Backend Logic Overview

* Webpage content is loaded using `WebBaseLoader`
* Content is sent to an LLM via HuggingFace Inference API
* The generated summary is cached in memory
* Repeated requests for the same URL return cached results instantly

---

## Frontend Setup (Chrome Extension)

### Open Chrome Extensions Page

```
chrome://extensions
```

---

### Enable Developer Mode

Turn on **Developer Mode** (top-right corner).

---

### Load the Extension

1. Click **Load unpacked**
2. Select the `frontend/` folder
3. The extension will appear in your toolbar

---

### Using the Extension

1. Open any website
2. Click the **Website Summarizer** extension icon
3. Wait a few seconds
4. Read the summarized content in the popup

---

## How It Works

1. Chrome Extension reads the active tab URL
2. Sends the URL to the FastAPI backend
3. Backend fetches webpage content
4. LLM generates a summary
5. Summary is returned and displayed in the popup

---

## Limitations

* Some websites may block content scraping
* Large pages may take longer to summarize
* Cache is in-memory and resets on server restart
* Backend must be running locally for the extension to work

---

## Future Improvements

* Add loading spinner and better UI feedback
* Persistent caching using Redis or a database
* Bullet-point or structured summaries
* Deploy backend to cloud (no localhost dependency)
* Authentication and rate limiting

---

## Author

**Shayan Sarkar**
Computer Science Student
(Interested in AI)

---

## License

This project is open-source and intended for educational purposes.
