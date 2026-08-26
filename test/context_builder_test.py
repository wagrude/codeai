from src.repository_retriever import RepositoryRetriever
from src.context_builder import build_context


retriever = RepositoryRetriever(
    ".",
    chunk_size=10,
    overlap=2
)

print("Building repository index...")

retriever.build_index()

results = retriever.search(
    "Where is vector similarity calculated?",
    top_k=3
)

context = build_context(results)

print("\nGenerated Context:\n")
print(context)
