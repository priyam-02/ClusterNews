# 📰 Global News Topic Tracker

An AI-powered web application that scrapes the latest headlines from Google News, clusters related articles using vector embeddings, and summarizes each topic using a local LLaMA 3.1 model—all in your browser.

---
## 🎥 Demo


https://github.com/user-attachments/assets/3eb9605b-a3a1-42fa-93b4-8f03f8e5b533


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
ollama run llama3.1
```

> ✅ Make sure Ollama is running on `http://localhost:11434` before starting the app.

### 4. Run the Flask app

```bash
python3 app.py
```

Navigate to `http://localhost:5000` in your browser.

---

## 🖼️ Screenshots
<img width="1920" alt="Screenshot 2025-05-12 at 9 48 45 PM (2)" src="https://github.com/user-attachments/assets/6f68212c-de42-4ffa-89f6-8167eb58726d" />

<img width="1920" alt="Screenshot 2025-05-12 at 9 48 54 PM (2)" src="https://github.com/user-attachments/assets/cd830096-2baf-4543-b1ac-3a1b375f4cf7" />

<img width="1920" alt="Screenshot 2025-05-12 at 9 51 18 PM (2)" src="https://github.com/user-attachments/assets/4655a9ed-4771-4073-8e01-0afa94043d69" />


---

## 🛡️ Disclaimer

This is a personal project intended for educational and demonstration purposes. All content is retrieved from public sources and summarized locally.
