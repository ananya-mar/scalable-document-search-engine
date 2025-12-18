import time
import psutil
import os

def benchmark_query(search_fn, query):
    start = time.time()
    results = search_fn(query)
    latency = (time.time() - start) * 1000
    return latency, results

def memory_usage_mb():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)
