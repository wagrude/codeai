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

        query = np.array(
            query_embedding,
            dtype=np.float32
        )

        query_norm = np.linalg.norm(query)

        if query_norm == 0:
            return []

        results = []

        for entry in self.entries:
            vector = np.array(
                entry["embedding"],
                dtype=np.float32
            )

            vector_norm = np.linalg.norm(vector)

            if vector_norm == 0:
                continue

            score = np.dot(query, vector) / (
                query_norm * vector_norm
            )

            results.append({
                "chunk": entry["chunk"],
                "score": float(score)
            })

        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        selected = []
        selected_ranges = {}

        for result in results:
            chunk = result["chunk"]
            file_path = chunk["file"]

            start_line = chunk["start_line"]
            end_line = chunk["end_line"]

            overlap_found = False

            for existing_start, existing_end in selected_ranges.get(
                file_path, []
            ):
                if (
                    start_line <= existing_end
                    and end_line >= existing_start
                ):
                    overlap_found = True
                    break

            if overlap_found:
                continue

            selected.append(result)

            selected_ranges.setdefault(
                file_path, []
            ).append(
                (start_line, end_line)
            )

            if len(selected) == top_k:
                break

        return selected

    def save(self, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.entries, file)

    def load(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            self.entries = json.load(file)