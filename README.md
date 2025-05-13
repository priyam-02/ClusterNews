# 📰 Global News Topic Tracker

An AI-powered web application that scrapes the latest headlines from Google News, clusters related articles using vector embeddings, and summarizes each topic using a local LLaMA 3.1 model—all in your browser.

---

## 🌟 Features

- 🔍 Real-time scraping of trending headlines from Google News
- 🧠 Clustering using `all-mpnet-base-v2` sentence embeddings + HDBSCAN
- 📝 Summarization using a local LLaMA 3.1 model via Ollama
- 💻 Fully local processing — no tracking, no external API calls
- 🎨 Responsive, dark-themed UI with elegant transitions and refresh support
- ⚡ Built with Flask + TailwindCSS + vanilla JavaScript

---

## 🧱 Tech Stack

| Layer         | Tool                                      |
| ------------- | ----------------------------------------- |
| Backend       | Python, Flask                             |
| Scraping      | Selenium                                  |
| Embedding     | `sentence-transformers/all-mpnet-base-v2` |
| Clustering    | HDBSCAN + cosine distance                 |
| Summarization | LLaMA 3.1 via Ollama API                  |
| Frontend      | HTML, TailwindCSS, JavaScript             |

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/global-news-tracker.git
cd global-news-tracker
```

### 2. Install dependencies

Ensure you have Python 3.10+ and `pip` installed.

```bash
pip install -r requirements.txt
```

### 3. Start Ollama (for local LLaMA model)

Install and run Ollama locally: [https://ollama.com](https://ollama.com)

```bash
ollama run llama3
```

> ✅ Make sure Ollama is running on `http://localhost:11434` before starting the app.

### 4. Run the Flask app

```bash
python app.py
```

Navigate to `http://localhost:5000` in your browser.

---

## 🖼️ Screenshots

---

## 🛡️ Disclaimer

This is a personal project intended for educational and demonstration purposes. All content is retrieved from public sources and summarized locally.
