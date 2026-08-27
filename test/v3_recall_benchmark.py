import re

from src.repository_retriever import RepositoryRetriever


PROJECT = "test"

retriever = RepositoryRetriever(
    PROJECT,
    chunk_size=10,
    overlap=2
)

retriever.build_index()

queries = [
    {
        "query": "Where is the multiply function?",
        "expected": "int multiply"
    },
    {
        "query": "Where is the add function?",
        "expected": "int add"
    },
    {
        "query": "Where is the main function?",
        "expected": "int main"
    },
    {
        "query": "Where are the program input variables?",
        "expected": "int x = 10"
    },
    {
        "query": "Where is the y variable initialized?",
        "expected": "int y = 20"
    },
    {
        "query": "Where is addition performed?",
        "expected": "int sum = add"
    },
    {
        "query": "Where is multiplication performed?",
        "expected": "int product = multiply"
    },
    {
        "query": "Where is the result printed?",
        "expected": "print_result"
    },
    {
        "query": "Where is printf used?",
        "expected": "printf"
    },
    {
        "query": "Where is the multiply function called?",
        "expected": "multiply(x, y)"
    },
    {
        "query": "Where is the add function called?",
        "expected": "add(x, y)"
    },
    {
        "query": "Where does the program return zero?",
        "expected": "return 0"
    },
    {
        "query": "Where is the result message formatted?",
        "expected": "Result: %d"
    },
    {
        "query": "Where are the standard libraries included?",
        "expected": "#include"
    },
    {
        "query": "Where is the product calculated?",
        "expected": "int product"
    },
    {
        "query": "Where is the sum calculated?",
        "expected": "int sum"
    },
    {
        "query": "Where does the program start execution?",
        "expected": "int main"
    },
    {
        "query": "Which function prints the result?",
        "expected": "void print_result"
    },
]


def contains_expected(result, expected):
    content = result["chunk"]["content"]
    return re.search(re.escape(expected), content) is not None


total = len(queries)

hits_at_1 = 0
hits_at_3 = 0
hits_at_5 = 0

reciprocal_rank_sum = 0


for item in queries:

    query = item["query"]
    expected = item["expected"]

    results = retriever.search(
        query,
        top_k=5
    )

    rank_found = None

    for rank, result in enumerate(results, start=1):
        if contains_expected(result, expected):
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
    print(f"Expected: {expected}")
    print(f"Found at rank: {rank_found}")


recall_at_1 = hits_at_1 / total
recall_at_3 = hits_at_3 / total
recall_at_5 = hits_at_5 / total
mrr = reciprocal_rank_sum / total


print("\n--- V3 Retrieval Results ---")

print(f"Recall@1: {recall_at_1:.2%}")
print(f"Recall@3: {recall_at_3:.2%}")
print(f"Recall@5: {recall_at_5:.2%}")
print(f"MRR:      {mrr:.4f}")
