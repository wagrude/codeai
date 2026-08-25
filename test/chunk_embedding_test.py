from src.chunker import chunk_file
from src.embedder import embed_text


chunks = chunk_file(
    "test/sample.c",
    chunk_size=10,
    overlap=2
)

for i, chunk in enumerate(chunks, start=1):
    embedding = embed_text(chunk["content"])

    print(
        f"Chunk {i}: "
        f"lines {chunk['start_line']}-{chunk['end_line']} "
        f"→ {len(embedding)} dimensions"
    )