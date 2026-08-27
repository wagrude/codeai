import re
import time
import tracemalloc

from src.repository_retriever import RepositoryRetriever


PROJECT = "test/benchmark_large"

retriever = RepositoryRetriever(
    PROJECT,
    chunk_size=20,
    overlap=5
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
    {
        "query": "Where is the User structure defined?",
        "expected": "typedef struct",
        "file": "user.h"
    },
    {
        "query": "Where is a user initialized?",
        "expected": "init_user",
        "file": "user.c"
    },
    {
        "query": "Where is a user deactivated?",
        "expected": "deactivate_user",
        "file": "user.c"
    },
    {
        "query": "Where is user activity checked?",
        "expected": "is_user_active",
        "file": "user.c"
    },
    {
        "query": "Where is the maximum number of users defined?",
        "expected": "MAX_USERS",
        "file": "config.h"
    },
    {
        "query": "Where are users stored?",
        "expected": "static User users",
        "file": "database.c"
    },
    {
        "query": "Where is a user added to the database?",
        "expected": "database_add_user",
        "file": "database.c"
    },
    {
        "query": "Where is a user searched by ID?",
        "expected": "database_find_user",
        "file": "database.c"
    },
    {
        "query": "Where is a user removed?",
        "expected": "database_remove_user",
        "file": "database.c"
    },
    {
        "query": "Where is the database user count returned?",
        "expected": "database_user_count",
        "file": "database.c"
    },
    {
        "query": "Where is authentication implemented?",
        "expected": "authenticate_user",
        "file": "auth.c"
    },
    {
        "query": "Where is admin authorization checked?",
        "expected": "authorize_user",
        "file": "auth.c"
    },
    {
        "query": "Where is admin access determined by user ID?",
        "expected": "user->id == 1",
        "file": "auth.c"
    },
    {
        "query": "Where are informational messages logged?",
        "expected": "log_info",
        "file": "logger.c"
    },
    {
        "query": "Where are error messages logged?",
        "expected": "log_error",
        "file": "logger.c"
    },
    {
        "query": "Where are user actions logged?",
        "expected": "log_user_action",
        "file": "logger.c"
    },
    {
        "query": "Where does the application initialize the database?",
        "expected": "database_init",
        "file": "main.c"
    },
    {
        "query": "Where is the admin user created?",
        "expected": 'init_user(&admin',
        "file": "main.c"
    },
    {
        "query": "Where does the application authenticate a user?",
        "expected": "authenticate_user(user)",
        "file": "main.c"
    },
    {
        "query": "Where does the application check admin authorization?",
        "expected": 'authorize_user(user, "admin")',
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

    print(f"\nQuery: {query}")
    print(f"Expected file: {expected_file}")
    print(f"Expected: {expected}")
    print(f"Found at rank: {rank_found}")
    print(f"Latency: {latency * 1000:.2f} ms")


recall_at_1 = hits_at_1 / total
recall_at_3 = hits_at_3 / total
recall_at_5 = hits_at_5 / total
mrr = reciprocal_rank_sum / total
average_latency = total_latency / total


print("\n--- V3 Large Benchmark ---")

print(f"Queries:       {total}")
print(f"Recall@1:      {recall_at_1:.2%}")
print(f"Recall@3:      {recall_at_3:.2%}")
print(f"Recall@5:      {recall_at_5:.2%}")
print(f"MRR:           {mrr:.4f}")
print(f"Avg latency:   {average_latency * 1000:.2f} ms")
print(f"Indexing time: {index_time:.4f} seconds")
print(f"Chunks:        {len(retriever.store.entries)}")
print(f"Peak memory:   {peak / 1024 / 1024:.2f} MB")
