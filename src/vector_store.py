import json
import numpy as np


class VectorStore:

    def __init__(self):
        self.entries = []

    def add(self, chunk, embedding):
        self.entries.append({
            "chunk": chunk,
            "embedding": embedding
        })

    def search(self, query_embedding, top_k=5):
        if not self.entries:
            return []

        query = np.array(query_embedding, dtype=np.float32)

        results = []

        for entry in self.entries:
            vector = np.array(
                entry["embedding"],
                dtype=np.float32
            )

            score = np.dot(query, vector) / (
                np.linalg.norm(query) * np.linalg.norm(vector)
            )

            results.append({
                "chunk": entry["chunk"],
                "score": float(score)
            })

        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        return results[:top_k]

    def save(self, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.entries, file)

    def load(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            self.entries = json.load(file)
