# Pair Exercise #4: Sequential and Concurrent Downloading
# Varuzhan Shahidzadeh, Partner: Daniel Abalusi

"""
pe4.py

Section A: 
Section B: 
"""

import re
import time
from concurrent.futures import ThreadPoolExecutor

import wikipedia

# 1. Search for topics related to 'generative artificial intelligence'
topics = wikipedia.search("generative artificial intelligence")
print(f"Found {len(topics)} topics: {topics}")

# 2. Iterate over topics sequentially
for topic in topics:
    try:
        page = wikipedia.page(topic, auto_suggest=False)
    except (wikipedia.exceptions.DisambiguationError,
            wikipedia.exceptions.PageError) as err:
        print(f"Skipping '{topic}': {type(err).__name__}")
        continue

    title = page.title
    references = page.references

    # page.references is a list, so join into a string with one URL per line
    with open(f"{safe_filename(title)}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(references))

    print(f"Wrote {len(references)} references for '{title}'")

    # 3. Print total elapsed time for ALL topics
    end = time.perf_counter()
    print(f"Section A (sequential) finished in {end - start:.2f} seconds")
