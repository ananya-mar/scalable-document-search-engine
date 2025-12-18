from ingestion.loader import load_documents
from preprocessing.tokenizer import tokenize
from indexing.inverted_index import InvertedIndex
from indexing.index_store import save_index, load_index
from query.query_processor import QueryProcessor
from evaluation.benchmarks import benchmark_query, memory_usage_mb
import os

DATA_DIR = "data"
INDEX_FILE = "index.pkl"

def build_index():
    docs = load_documents(DATA_DIR)
    index = InvertedIndex()

    for doc_id, text in docs.items():
        tokens = tokenize(text)
        index.add_document(doc_id, tokens)

    save_index(index, INDEX_FILE)
    print(f"Indexed {len(docs)} documents.")

def search_loop():
    index = load_index(INDEX_FILE)
    qp = QueryProcessor(index, len(index.doc_lengths))

    while True:
        q = input("\nSearch (or 'exit'): ")
        if q == "exit":
            break

        latency, results = benchmark_query(qp.search, q)
        print(f"Latency: {latency:.2f} ms")

        for doc_id, score in results[:5]:
            print(f"Doc {doc_id} | Score: {score:.4f}")

        print(f"Memory Usage: {memory_usage_mb():.2f} MB")

if __name__ == "__main__":
    if not os.path.exists(INDEX_FILE):
        build_index()
    search_loop()
