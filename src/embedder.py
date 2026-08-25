import ollama

MODEL = "nomic-embed-text"


def embed_text(text):
    response = ollama.embed(
        model=MODEL,
        input=text
    )

    return response["embeddings"][0]