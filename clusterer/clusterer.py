# # clusterer.py

# from typing import List, Dict
# from sentence_transformers import SentenceTransformer
# import hdbscan
# import numpy as np


# # Load a sentence transformer model
# # This converts text to 384-dimensional embeddings that capture meaning
# model = SentenceTransformer("all-mpnet-base-v2")


# def cluster_headlines(headlines: List[str]) -> Dict[int, List[str]]:
#     """
#     Clusters similar headlines into groups using HDBSCAN.

#     Args:
#         headlines (List[str]): A list of raw news headline strings.

#     Returns:
#         Dict[int, List[str]]: A dictionary mapping each cluster ID
#                               to a list of headlines in that group.
#                               Cluster -1 = noise/outliers.
#     """

#     print("🔍 Step 1: Generating sentence embeddings...")
#     # Turn headlines into vector embeddings
#     embeddings = model.encode(headlines)

#     print("🔗 Step 2: Performing density-based clustering with HDBSCAN...")
#     # Create and fit the HDBSCAN model
#     clusterer = hdbscan.HDBSCAN(
#         min_cluster_size=2,  # Minimum size for a group to be a cluster
#         min_samples=1,  # Lower value = less strict = fewer outliers
#         metric="euclidean",  # Keep this for embedding space
#         cluster_selection_method="eom",  # Use "eom" for better cluster boundaries
#         cluster_selection_epsilon=0.8,  # ↑ Increased this to include looser points
#     )
#     cluster_labels = clusterer.fit_predict(embeddings)

#     print("🧠 Step 3: Organizing headlines by cluster...")
#     clusters: Dict[int, List[str]] = {}

#     for label, headline in zip(cluster_labels, headlines):
#         # label == -1 means the item was considered "noise" (no cluster)
#         if label not in clusters:
#             clusters[label] = []
#         clusters[label].append(headline)

#     print(f"✅ Found {len(clusters)} total clusters (including noise).")
#     return clusters


# # if __name__ == "__main__":
# #     sample_headlines = [
# #         "Trump meets with Canadian PM",
# #         "Biden visits Canada for trade deal",
# #         "Apple unveils new MacBook",
# #         "Google launches new AI model",
# #         "Elon Musk's Tesla expands to Canada",
# #         "Microsoft adds AI to Excel",
# #         "Pope addresses crowd at Vatican",
# #     ]

# #     clusters = cluster_headlines(sample_headlines)

# #     for cluster_id, headlines in clusters.items():
# #         print(f"\n🧠 Cluster {cluster_id}:")
# #         for h in headlines:
# #             print("  •", h)


from typing import List, Dict
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_distances
import hdbscan
import numpy as np


# 🧠 Load a powerful multilingual embedding model
model = SentenceTransformer("all-mpnet-base-v2")  # Or multilingual-e5-base


def cluster_headlines(headlines: List[str]) -> Dict[int, List[str]]:
    """
    Cluster related headlines using Sentence Transformers + HDBSCAN.

    Args:
        headlines (List[str]): List of news headlines.

    Returns:
        Dict[int, List[str]]: Cluster ID mapped to list of headlines. -1 = noise.
    """

    print("🔍 Step 1: Generating sentence embeddings...")
    # embeddings = model.encode(headlines, convert_to_numpy=True)
    texts = [item["text"] for item in headlines]
    embeddings = model.encode(texts, convert_to_numpy=True)

    print("📐 Step 2: Calculating cosine distances between headlines...")
    distance_matrix = cosine_distances(embeddings).astype(np.float64)

    print("🔗 Step 3: Performing density-based clustering with HDBSCAN...")
    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=2,
        min_samples=1,
        metric="precomputed",  # Required when passing distance matrix
        cluster_selection_epsilon=0.3,
    )
    cluster_labels = clusterer.fit_predict(distance_matrix)

    print("🧠 Step 4: Organizing headlines by cluster...")
    clusters: Dict[int, List[str]] = {}
    for label, headline in zip(cluster_labels, headlines):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(headline)

    print(f"✅ Found {len(clusters)} total clusters (including noise).")
    return clusters
