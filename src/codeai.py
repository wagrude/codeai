from src.repository_retriever import RepositoryRetriever
from src.context_builder import build_context
from src.llm import generate


class CodeAI:

    def __init__(self, project_path):
        self.retriever = RepositoryRetriever(project_path)

    def ask(self, question, top_k=5):
        self.retriever.build_index()

        results = self.retriever.search(
            question,
            top_k=top_k
        )

        context = build_context(results)

        print("\n--- RETRIEVED CONTEXT ---\n")
        print(context)
        print("\n--- END CONTEXT ---\n")

        prompt = f"""
You are CodeAI, an AI coding assistant.

Answer the user's question using the provided repository context.

If the context does not contain enough information, say so clearly.
Do not invent code or repository details.

Repository context:

{context}

User question:

{question}
"""

        return generate(prompt)