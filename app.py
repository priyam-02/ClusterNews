# from scraper_selenium.scraper_selenium import scrape_google_news_selenium
# from clusterer.clusterer import cluster_headlines
# from summarizer.summarizer import summarize_cluster
# from organizer.organizer import organize_clusters

# print("📥 Scraping news...")
# news_items = scrape_google_news_selenium()

# # Deduplicate based on headline text
# seen = set()
# unique_news_items = []
# for item in news_items:
#     if item["headline"] not in seen:
#         seen.add(item["headline"])
#         unique_news_items.append(item)

# headlines = [item["headline"] for item in unique_news_items]

# print("🧠 Clustering headlines...")
# clusters = cluster_headlines(headlines)

# # Display results with summarization
# for cluster_id, headlines in clusters.items():
#     print(f"\n🧠 Cluster {cluster_id}:")
#     for hl in headlines:
#         print(f"  • {hl}")

#     # Add this line to summarize each cluster
#     summary = summarize_cluster(headlines)
#     print(f"📝 Summary: {summary}")

# # Summarize and organize
# print("\n📊 Organizing topics...")
# cluster_df = organize_clusters(clusters)

# # Display organized output
# for _, row in cluster_df.iterrows():
#     print(f"\n🧠 Cluster {row['cluster_id']} ({row['num_headlines']} headlines):")
#     print(f"📌 Summary: {row['summary']}")
#     for headline in row["headlines"]:
#         print(f"  • {headline}")


from flask import Flask, render_template, jsonify
from scraper_selenium.scraper_selenium import scrape_google_news_selenium
from clusterer.clusterer import cluster_headlines
from summarizer.summarizer import summarize_cluster
from organizer.organizer import organize_clusters

app = Flask(__name__)


@app.route("/")
# def index():
#     loading = True
#     # 📥 Scrape news
#     news_items = scrape_google_news_selenium()

#     # Deduplicate
#     seen = set()
#     unique_news_items = []
#     for item in news_items:
#         if item["headline"] not in seen:
#             seen.add(item["headline"])
#             unique_news_items.append(item)

#     # 🧠 Cluster
#     headlines = [item["headline"] for item in unique_news_items]
#     clusters = cluster_headlines(headlines)

#     # 📊 Summarize & organize
#     cluster_df = organize_clusters(clusters, summarize_cluster)

#     return render_template(
#         "index.html", clusters=cluster_df.to_dict(orient="records"), loading=False
#     )


# if __name__ == "__main__":
#     app.run(debug=True)
def index():
    # Initial page with loading UI
    return render_template("index.html", clusters=[], loading=True)


@app.route("/data")
def load_data():
    # 📥 Scrape news
    news_items = scrape_google_news_selenium()

    # Deduplicate
    seen = set()
    unique_news_items = []
    for item in news_items:
        if item["headline"] not in seen:
            seen.add(item["headline"])
            unique_news_items.append({"text": item["headline"], "url": item["url"]})

    # 🧠 Cluster
    # headlines = [item["headline"] for item in unique_news_items]
    headlines = unique_news_items  # Keep full objects: {text, url}
    clusters = cluster_headlines(headlines)

    # 📊 Summarize & organize
    cluster_df = organize_clusters(clusters, summarize_cluster)
    cleaned_clusters = cluster_df[cluster_df["cluster_id"] != -1]

    return jsonify(cleaned_clusters.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=False)
