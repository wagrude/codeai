from src.embedder import embed_text


text = "linked list insertion function"

embedding = embed_text(text)

print("Embedding dimensions:", len(embedding))
print("First 10 values:", embedding[:10])