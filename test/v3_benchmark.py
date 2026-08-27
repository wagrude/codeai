import time
import tracemalloc

from src.repository_retriever import RepositoryRetriever


PROJECT = "test"


retriever = RepositoryRetriever(
    PROJECT,
    chunk_size=10,
    overlap=2
)


print("Building index...")

tracemalloc.start()

start = time.perf_counter()

retriever.build_index()

index_time = time.perf_counter() - start

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()


print(f"Indexing time: {index_time:.4f} seconds")
print(f"Chunks indexed: {len(retriever.store.entries)}")
print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")


queries = [
    "Where is the multiply function?",
    "Where is the add function?",
    "Where is the main function?",
]


print("\nRetrieval Benchmark")


for query in queries:

    start = time.perf_counter()

    results = retriever.search(
        query,
        top_k=3
    )

    latency = time.perf_counter() - start

    print(f"\nQuery: {query}")
    print(f"Latency: {latency * 1000:.2f} ms")

    for rank, result in enumerate(results, start=1):

        chunk = result["chunk"]

        print(
            f"  {rank}. "
            f"score={result['score']:.4f} "
            f"lines={chunk['start_line']}-{chunk['end_line']}"
        )
