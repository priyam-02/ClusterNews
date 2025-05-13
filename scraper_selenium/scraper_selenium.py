# scraper_selenium.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def scrape_google_news_selenium():
    # Setup headless Chrome
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    print("🌐 Opening Google News...")

    driver = webdriver.Chrome(options=options)
    driver.get("https://news.google.com")
    time.sleep(5)

    article_elements = driver.find_elements(By.TAG_NAME, "article")
    print(f"🔍 Found {len(article_elements)} <article> blocks.")

    articles = []

    for article in article_elements:
        try:
            links = article.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                text = link.text.strip()

                if href and text and "/read/" in href:
                    if href.startswith("./"):
                        href = "https://news.google.com" + href[1:]
                    articles.append({"headline": text, "url": href})
                    break
        except Exception as e:
            print(f"⚠️ Skipping article due to error: {e}")

    driver.quit()
    print(f"\n✅ Scraper finished. Valid news articles: {len(articles)}\n")
    return articles


if __name__ == "__main__":
    articles = scrape_google_news_selenium()
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['headline']}\n   ➤ {article['url']}")
