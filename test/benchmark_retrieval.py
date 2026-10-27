
import math
import statistics
import time

from src.retriever import Retriever


FILE_PATH = "test/sample.c"
CHUNK_SIZE = 10
OVERLAP = 2
TOP_K = 5
REPEATS = 3


# Each query has a known function definition line.
QUERIES = [
    {
        "query": "Where is the add function?",
        "definition_line": 4,
    },
    {
        "query": "Where is the multiply function?",
        "definition_line": 8,
    },
    {
        "query": "Where is the print_result function?",
        "definition_line": 13,
    },
    {
        "query": "Where is the main function?",
        "definition_line": 17,
    },
]


def is_relevant(result, query):
    chunk = result["chunk"]

    return (
        chunk["start_line"]
        <= query["definition_line"]
        <= chunk["end_line"]
    )


def percentile_95(values):
    ordered = sorted(values)
    index = math.ceil(0.95 * len(ordered)) - 1
    return ordered[index]


def main():
    retriever = Retriever(
        FILE_PATH,
        chunk_size=CHUNK_SIZE,
        overlap=OVERLAP,
    )

    # Measure indexing time.
    start = time.perf_counter()
    retriever.build_index()
    indexing_time = time.perf_counter() - start

    reciprocal_ranks = []
    recall_at_1 = []
    recall_at_5 = []
    latencies = []

    for item in QUERIES:
        results = None

        # Repeat each query for latency measurements.
        for _ in range(REPEATS):
            start = time.perf_counter()

            results = retriever.search(
                item["query"],
                top_k=TOP_K,
            )

            latency_ms = (
                time.perf_counter() - start
            ) * 1000

            latencies.append(latency_ms)

        # Find the rank of the first relevant chunk.
        relevant_ranks = [
            rank
            for rank, result in enumerate(results, start=1)
            if is_relevant(result, item)
        ]

        first_relevant_rank = (
            relevant_ranks[0]
            if relevant_ranks
            else None
        )

        reciprocal_ranks.append(
            1 / first_relevant_rank
            if first_relevant_rank is not None
            else 0
        )

        recall_at_1.append(
            int(first_relevant_rank == 1)
        )

        recall_at_5.append(
            int(
                first_relevant_rank is not None
                and first_relevant_rank <= 5
            )
        )

        displayed_rank = (
            first_relevant_rank
            if first_relevant_rank is not None
            else "MISS"
        )

        print(f"\nQuery: {item['query']}")
        print(
            "Expected definition line: "
            f"{item['definition_line']}"
        )
        print(
            f"First relevant rank: {displayed_rank}"
        )

        for rank, result in enumerate(results, start=1):
            chunk = result["chunk"]

            print(
                f"  Rank {rank}: "
                f"lines {chunk['start_line']}-"
                f"{chunk['end_line']} "
                f"| score={result['score']:.4f}"
            )

    print("\n=== CodeAI V3 Retrieval Benchmark ===")
    print(f"File: {FILE_PATH}")
    print(f"Queries: {len(QUERIES)}")
    print(f"Repeats per query: {REPEATS}")
    print(f"Indexing time: {indexing_time:.3f} seconds")
    print(
        "Median query latency: "
        f"{statistics.median(latencies):.2f} ms"
    )
    print(
        "P95 query latency: "
        f"{percentile_95(latencies):.2f} ms"
    )
    print(
        f"Recall@1: {statistics.mean(recall_at_1):.2%}"
    )
    print(
        f"Recall@5: {statistics.mean(recall_at_5):.2%}"
    )
    print(
        f"MRR: {statistics.mean(reciprocal_ranks):.4f}"
    )


if __name__ == "__main__":
    main()
