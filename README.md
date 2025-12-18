# Scalable Document Search Engine (Information Retrieval System)

A document search engine implemented in Python to explore core **information retrieval** and **systems design** concepts such as inverted indexing, relevance ranking, and performance tradeoffs.

The project emphasizes **fundamental data structures and algorithms** over external search libraries, with a focus on **measurable performance, correctness, and extensible design**.

---

## Motivation

Search is a foundational systems problem involving:

- Efficient indexing  
- Fast query evaluation  
- Relevance ranking  
- Scalability tradeoffs  

This project was built to understand and implement these fundamentals directly, rather than relying on prebuilt search frameworks.

---

## Core Capabilities

- Folder-based ingestion of text documents  
- Tokenization, normalization, and stopword filtering  
- Custom inverted index for efficient term lookup  
- Positional inverted indexing for exact phrase queries  
- TF-IDF ranking for relevance scoring  
- Persistent index storage  
- Query latency and memory benchmarking  
- Minimal CLI interface to focus on backend logic  

---

## System Architecture

```text
search_engine/
│
├── ingestion/       # Document loading
├── preprocessing/   # Tokenization & filtering
├── indexing/        # Inverted & positional indexes
├── ranking/         # TF-IDF scoring
├── query/           # Query processing
├── storage/         # Index persistence
├── evaluation/      # Benchmarks
└── main.py
```


The system is modular by design, allowing indexing, ranking, and querying strategies to evolve independently.

---

## Design Decisions & Tradeoffs

### Inverted Index
An inverted index maps terms to document IDs, avoiding linear scans and enabling efficient retrieval. This mirrors the core structure used in large-scale search systems.

### Positional Indexing
Instead of storing only term frequencies, term positions are indexed to support phrase queries. This enables exact matching while preserving fast lookup.

### Ranking (TF-IDF)
TF-IDF was chosen because it:
- Is interpretable  
- Has predictable performance  
- Provides strong baseline relevance without ML overhead  

### In-Memory Indexing
Indexes are held in memory to minimize query latency. At larger scales, this design would naturally extend to disk-backed or distributed indexes.

### Persistence
Indexes are serialized to disk, allowing fast restarts and decoupling indexing cost from query serving.

---

## Query Types Supported

### Term Queries
Ranked using TF-IDF scoring.

Example:
```text
systems
```

### Phrase Queries
Resolved using positional index matching and ranked by phrase frequency.

Example:
```text
"distributed systems"
```

---

## Performance Evaluation

Benchmarks were run on synthetic corpora with realistic text density to evaluate scalability.

### Observed Latency

| Corpus Size | Query Type | Latency |
|------------|-----------|---------|
| 500 documents (large docs) | Term | ~0.9 ms |
| 500 documents (medium docs) | Term | 0.2–0.3 ms |
| 2,000 documents | Term | 0.22–0.58 ms |
| 2,000 documents | Phrase | ~3.5 ms |

Example runtime output:

```text
Query: systems
Latency: 1.08 ms
```
```text
Query: "distributed systems"
Latency: 3.51 ms
```


### Memory Usage
- ~54–55 MB for a 2,000-document corpus  
- Linear growth with corpus size  

These results indicate predictable scaling behavior and efficient inverted-index traversal.

---

## Limitations & Future Extensions

- Disk-backed indexing for larger datasets  
- Boolean query operators (AND / OR)  
- Snippet generation  
- Distributed indexing and sharding  
- API-based query serving  