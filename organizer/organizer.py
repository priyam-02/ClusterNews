# organizer/organizer.py

# from typing import List, Dict
# import pandas as pd
# from summarizer.summarizer import summarize_cluster


# # def organize_clusters(clusters: Dict[int, List[str]]) -> pd.DataFrame:
# #     """
# #     Organizes clustered headline data into a structured pandas DataFrame.

# #     Args:
# #         clusters (Dict[int, List[str]]): A dictionary mapping cluster IDs to headline lists.

# #     Returns:
# #         pd.DataFrame: Structured data with cluster_id, num_headlines, summary, and headlines.
# #     """
# #     print("📦 Organizing clusters into structured format...")

# #     organized = []
# #     for cluster_id, group in clusters.items():
# #         summary = summarize_cluster(group)
# #         organized.append(
# #             {
# #                 "cluster_id": cluster_id,
# #                 "num_headlines": len(group),
# #                 "summary": summary,
# #                 "headlines": group,
# #             }
# #         )

# #     df = pd.DataFrame(organized)
# #     print("✅ Clustered data structured into DataFrame.")
# #     return df


# def organize_clusters(clusters: Dict[int, List[str]], summarize_fn) -> pd.DataFrame:
#     """
#     Organizes clustered headlines into a structured DataFrame with summaries.

#     Args:
#         clusters (Dict[int, List[str]]): Cluster ID to headlines.
#         summarize_fn (function): Function that takes a list of headlines and returns a summary.

#     Returns:
#         pd.DataFrame: Structured cluster data.
#     """
#     organized_data = []
#     for cluster_id, headlines in clusters.items():
#         summary = summarize_fn(headlines)
#         organized_data.append(
#             {
#                 "cluster_id": cluster_id,
#                 "num_headlines": len(headlines),
#                 "summary": summary,
#                 "headlines": headlines,
#             }
#         )

#     return (
#         pd.DataFrame(organized_data)
#         .sort_values(by=lambda x: (x["cluster_id"] == -1, x["cluster_id"]))
#         .reset_index(drop=True)
#     )

from typing import List, Dict
import pandas as pd
from summarizer.summarizer import summarize_cluster


def organize_clusters(clusters: Dict[int, List[str]], summarize_fn) -> pd.DataFrame:
    """
    Organizes clustered headlines into a structured DataFrame with summaries.

    Args:
        clusters (Dict[int, List[str]]): Cluster ID to headlines.
        summarize_fn (function): Function that takes a list of headlines and returns a summary.

    Returns:
        pd.DataFrame: Structured cluster data.
    """
    organized_data = []
    for cluster_id, headlines in clusters.items():
        summary = summarize_fn(headlines)
        organized_data.append(
            {
                "cluster_id": cluster_id,
                "num_headlines": len(headlines),
                "summary": summary,
                "headlines": headlines,
            }
        )

    df = pd.DataFrame(organized_data)
    df["is_noise"] = df["cluster_id"] == -1  # Flag noise clusters
    df = df.sort_values(by=["is_noise", "cluster_id"]).drop(columns=["is_noise"])
    return df.reset_index(drop=True)
