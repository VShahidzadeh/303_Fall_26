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
