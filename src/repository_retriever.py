from src.scanner import scan_project
from src.chunker import chunk_file
from src.embedder import embed_text
from src.vector_store import VectorStore


class RepositoryRetriever:

    def __init__(self, project_path, chunk_size=80, overlap=10):
        self.project_path = project_path
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.store = VectorStore()

    def build_index(self):
        files = scan_project(self.project_path)

        for file_path in files:
            chunks = chunk_file(
                file_path,
                chunk_size=self.chunk_size,
                overlap=self.overlap
            )

            for chunk in chunks:
                embedding = embed_text(chunk["content"])
                self.store.add(chunk, embedding)

    def search(self, query, top_k=5):
        query_embedding = embed_text(query)

        return self.store.search(
            query_embedding,
            top_k=top_k
        )