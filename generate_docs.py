import os
import random

NUM_DOCS = 2000
DATA_DIR = "data"

os.makedirs(DATA_DIR, exist_ok=True)

sentences = [
    "search engines rely on inverted indexes to retrieve documents efficiently",
    "tf idf is a classical ranking algorithm in information retrieval systems",
    "python is widely used for backend services and rapid prototyping",
    "distributed systems focus on scalability availability and fault tolerance",
    "databases use indexing structures such as b trees and hash maps",
    "operating systems manage memory processes and file systems",
    "network protocols enable reliable and unreliable communication",
    "load balancing improves system throughput and reliability",
    "caching reduces latency by storing frequently accessed data",
    "concurrency and parallelism improve performance on multicore systems",
    "search ranking algorithms balance relevance freshness and popularity",
    "information retrieval systems must handle large scale text corpora",
    "document preprocessing includes tokenization normalization and filtering",
    "stopword removal reduces noise in textual data",
    "query latency is a critical metric in search engine design",
    "persistent storage allows indexes to be reused across sessions",
    "hash maps provide constant time access for indexing operations",
    "system benchmarks help evaluate performance under different workloads",
    "engineering tradeoffs are required between memory usage and speed",
    "scalable architectures allow systems to grow with increasing data volumes",
]

PARAGRAPHS_PER_DOC = (3, 6)
SENTENCES_PER_PARAGRAPH = (5, 10)

for i in range(NUM_DOCS):
    path = os.path.join(DATA_DIR, f"doc_{i}.txt")

    with open(path, "w", encoding="utf-8") as f:
        num_paragraphs = random.randint(*PARAGRAPHS_PER_DOC)

        for _ in range(num_paragraphs):
            paragraph_sentences = random.choices(
                sentences,
                k=random.randint(*SENTENCES_PER_PARAGRAPH)
            )
            paragraph = ". ".join(paragraph_sentences) + "."
            f.write(paragraph + "\n\n")

print(f"✅ Generated {NUM_DOCS} rich documents in '{DATA_DIR}/'")
