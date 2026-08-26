import os
import ollama


MODEL = "qwen3-coder:30b"


def generate_file_content(file_path, instruction):
    prompt = f"""
You are a code generation assistant.

Create the complete contents of the requested file.

Rules:
- Return ONLY the file content.
- Do not use markdown code fences.
- Do not explain anything.
- Generate valid code appropriate for the file extension.
- Follow the user's instruction exactly.

File path:

{file_path}

User instruction:

{instruction}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def propose_file(file_path, instruction):
    if os.path.exists(file_path):
        raise FileExistsError(
            f"File already exists: {file_path}"
        )

    content = generate_file_content(
        file_path,
        instruction
    )

    return content


def apply_file(file_path, content):
    parent = os.path.dirname(file_path)

    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
