import re
import time

from src.repository_retriever import RepositoryRetriever


PROJECT = "test/benchmark_project"

retriever = RepositoryRetriever(
    PROJECT,
    chunk_size=10,
    overlap=2
)

print("Building index...")

start = time.perf_counter()
retriever.build_index()
index_time = time.perf_counter() - start

print(f"Indexing time: {index_time:.4f} seconds")
print(f"Chunks indexed: {len(retriever.store.entries)}")


queries = [
    {
        "query": "Where is the add function implemented?",
        "expected": "int add",
        "file": "math.c"
    },
    {
        "query": "Where is the multiply function implemented?",
        "expected": "int multiply",
        "file": "math.c"
    },
    {
        "query": "Where are the math function declarations?",
        "expected": "int add(int a, int b)",
        "file": "math.h"
    },
    {
        "query": "Where are the math functions declared?",
        "expected": "int multiply(int a, int b)",
        "file": "math.h"
    },
    {
        "query": "Where is addition performed?",
        "expected": "return a + b",
        "file": "math.c"
    },
    {
        "query": "Where is multiplication performed?",
        "expected": "return a * b",
        "file": "math.c"
    },
    {
        "query": "Where is the main function?",
        "expected": "int main",
        "file": "main.c"
    },
    {
        "query": "Where are x and y initialized?",
        "expected": "int x = 10",
        "file": "main.c"
    },
    {
        "query": "Where is the sum calculated?",
        "expected": "int sum = add",
        "file": "main.c"
    },
    {
        "query": "Where is the product calculated?",
        "expected": "int product = multiply",
        "file": "main.c"
    },
    {
        "query": "Where is print_result implemented?",
        "expected": "void print_result",
        "file": "utils.c"
    },
    {
        "query": "Where is printf used?",
        "expected": "printf",
        "file": "utils.c"
    },
    {
        "query": "Where is the result formatting implemented?",
        "expected": '%s: %d',
        "file": "utils.c"
    },
    {
        "query": "Where is print_result declared?",
        "expected": "void print_result(const char *name, int value)",
        "file": "utils.h"
    },
    {
        "query": "Where are the utility functions declared?",
        "expected": "void print_result",
        "file": "utils.h"
    },
    {
        "query": "Which file includes math.h?",
        "expected": '#include "math.h"',
        "file": "main.c"
    },
    {
        "query": "Which file includes utils.h?",
        "expected": '#include "utils.h"',
        "file": "main.c"
    },
    {
        "query": "Where is the Sum result printed?",
        "expected": 'print_result("Sum", sum)',
        "file": "main.c"
    },
    {
        "query": "Where is the Product result printed?",
        "expected": 'print_result("Product", product)',
        "file": "main.c"
    },
    {
        "query": "Where does the program return zero?",
        "expected": "return 0",
        "file": "main.c"
    },
]


def matches(result, expected, expected_file):
    chunk = result["chunk"]

    return (
        re.search(re.escape(expected), chunk["content"])
        and chunk["file"].endswith(expected_file)
    )


total = len(queries)

hits_at_1 = 0
hits_at_3 = 0
hits_at_5 = 0
reciprocal_rank_sum = 0

total_latency = 0


for item in queries:

    query = item["query"]
    expected = item["expected"]
    expected_file = item["file"]

    start = time.perf_counter()

    results = retriever.search(
        query,
        top_k=5
    )

    latency = time.perf_counter() - start
    total_latency += latency

    rank_found = None

    for rank, result in enumerate(results, start=1):

        if matches(result, expected, expected_file):
            rank_found = rank
            break

    if rank_found == 1:
        hits_at_1 += 1

    if rank_found is not None and rank_found <= 3:
        hits_at_3 += 1

    if rank_found is not None and rank_found <= 5:
        hits_at_5 += 1

    if rank_found is not None:
        reciprocal_rank_sum += 1 / rank_found

    print(
        f"\nQuery: {query}"
        f"\nExpected file: {expected_file}"
        f"\nExpected: {expected}"
        f"\nFound at rank: {rank_found}"
        f"\nLatency: {latency * 1000:.2f} ms"
    )


recall_at_1 = hits_at_1 / total
recall_at_3 = hits_at_3 / total
recall_at_5 = hits_at_5 / total
mrr = reciprocal_rank_sum / total
average_latency = total_latency / total


print("\n--- V3 Multi-File Benchmark ---")

print(f"Queries:       {total}")
print(f"Recall@1:      {recall_at_1:.2%}")
print(f"Recall@3:      {recall_at_3:.2%}")
print(f"Recall@5:      {recall_at_5:.2%}")
print(f"MRR:           {mrr:.4f}")
print(f"Avg latency:   {average_latency * 1000:.2f} ms")
print(f"Indexing time: {index_time:.4f} seconds")
print(f"Chunks:        {len(retriever.store.entries)}")
