def build_context(results):
    if not results:
        return "No relevant code found."

    context_parts = []

    for i, result in enumerate(results, start=1):
        chunk = result["chunk"]
        score = result["score"]

        context_parts.append(
            f"""--- Context {i} ---
File: {chunk["file"]}
Lines: {chunk["start_line"]}-{chunk["end_line"]}
Relevance: {score:.4f}

{chunk["content"]}
"""
        )

    return "\n".join(context_parts)