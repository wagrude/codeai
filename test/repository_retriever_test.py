from src.repository_retriever import RepositoryRetriever


retriever = RepositoryRetriever(
    ".",
    chunk_size=10,
    overlap=2
)

print("Building repository index...")

retriever.build_index()

print("Searching...\n")

results = retriever.search(
    "Where is the vector similarity calculated?",
    top_k=5
)

for result in results:
    chunk = result["chunk"]

    print(f"Score: {result['score']:.4f}")
    print(f"File: {chunk['file']}")
    print(
        f"Lines: "
        f"{chunk['start_line']}-{chunk['end_line']}"
    )
    print(chunk["content"])
    print("-" * 60)
