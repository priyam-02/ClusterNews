# summarizer.py

# from typing import List
# import os
# from openai import OpenAI


# # 🛠️ Configure client for local Ollama
# client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")


# def summarize_cluster(headlines: List[str]) -> str:
#     prompt = (
#         "The following are headlines from a news cluster.\n"
#         "Summarize the following news headlines into 1–2 concise sentences: \n\n **without changing named entities or facts**."
#         + "\n".join(f"- {h}" for h in headlines)
#         + "\n\nSummary:"
#     )

#     # ✅ Use the modern `client.chat.completions.create()` method
#     response = client.chat.completions.create(
#         model="llama3.1",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=1.0,
#         max_tokens=100,
#     )

#     return response.choices[0].message.content.strip()

# from typing import List, Dict
# from transformers import pipeline

# # 🧠 Load a summarization pipeline using a pre-trained model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


# def summarize_cluster(headlines: List[str]) -> str:
#     """
#     Summarize a cluster of related news headlines into 1–2 sentences.

#     Args:
#         headlines (List[str]): A list of related headlines (1 cluster).

#     Returns:
#         str: A concise summary representing the main topic.
#     """

#     # 📝 Join all headlines into a single text block for the LLM
#     text = " ".join(headlines)

#     # 🧹 Optional: Truncate if it's too long (BART has a limit of 1024 tokens)
#     text = text[:1024]

#     input_length = len(text.split())
#     max_len = min(100, int(input_length * 0.7))
#     max_len = max(max_len, 20)

#     min_len = min(30, max_len - 1)

#     # 🤖 Generate the summary
#     result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)

#     return result[0]["summary_text"]


# summarizer.py

from typing import List
from openai import OpenAI

# ✅ Connect to local Ollama instance with LLaMA 3.1
client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")


def summarize_cluster(headlines: List[str]) -> str:
    """
    Summarize a cluster of related news headlines into 1–2 sentences using LLaMA 3.1 locally via Ollama.

    Args:
        headlines (List[str]): A list of related news headlines.

    Returns:
        str: A concise summary representing the main topic.
    """
    # 📝 Build a clear prompt with bullet formatting
    bullet_points = "\n".join(f"- {h}" for h in headlines)
    prompt = (
        "Summarize the following news headlines in the style of a concise news blurb (max 1 sentences). "
        "Keep named entities accurate, don't fabricate details, and don't merge unrelated topics.\n\n"
        f"{bullet_points}\n\nSummary:"
    )

    # 🧠 Call local LLaMA via OpenAI-compatible API
    try:
        response = client.chat.completions.create(
            model="llama3.1",  # Or "llama3.1:8b" depending on your model setup
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a concise, factual news summarizer. Do not use phrases like 'Here is a summary'. "
                        "Just return a direct 1 sentence summary in a clear, informative tone."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=150,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Summarization failed: {e}"


# if __name__ == "__main__":
#     headlines = [
#         "India launches missile attacks on Pakistan",
#         "Tensions escalate after India fires missiles into Pakistani-controlled territory",
#         "India launches missile attacks on Pakistan",
#         "India fires missiles into Pakistani territory in response to Kashmir attack, killing 8 people",
#     ]
#     print("🧠 Summary:", summarize_cluster(headlines))
