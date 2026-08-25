from src.chunker import chunk_file
from src.embedder import embed_text
from src.vector_store import VectorStore


chunks = chunk_file(
    "test/sample.c",
    chunk_size=10,
    overlap=2
)

store = VectorStore()

for chunk in chunks:
    embedding = embed_text(chunk["content"])
    store.add(chunk, embedding)


query = "Where is the multiply function?"

query_embedding = embed_text(query)

results = store.search(
    query_embedding,
    top_k=3
)

for result in results:
    chunk = result["chunk"]

    print(
        f"\nScore: {result['score']:.4f}"
    )

    print(
        f"File: {chunk['file']}"
    )

    print(
        f"Lines: "
        f"{chunk['start_line']}-{chunk['end_line']}"
    )

    print(chunk["content"])