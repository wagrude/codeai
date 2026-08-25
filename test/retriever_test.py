from src.retriever import Retriever


retriever = Retriever(
    "test/sample.c",
    chunk_size=10,
    overlap=2
)

retriever.build_index()

results = retriever.search(
    "Where is the multiply function?",
    top_k=3
)

for result in results:
    chunk = result["chunk"]

    print(f"\nScore: {result['score']:.4f}")
    print(
        f"Lines: "
        f"{chunk['start_line']}-{chunk['end_line']}"
    )
    print(chunk["content"])
