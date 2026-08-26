from src.editor import create_diff


def generate_modified_content(old_content, instruction):
    import ollama

    prompt = f"""
You are a code modification assistant.

Modify the provided code according to the user's instruction.

Rules:
- Return ONLY the complete modified file content.
- Do not use markdown code fences.
- Do not explain anything.
- Preserve all existing code that does not need to change.

User instruction:

{instruction}

Current file:

{old_content}
"""

    response = ollama.chat(
        model="qwen3-coder:30b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


file_path = "test/edit_target.c"

with open(file_path, "r", encoding="utf-8") as file:
    old_content = file.read()


instruction = "Change the add function so it returns a + b + 10."


new_content = generate_modified_content(
    old_content,
    instruction
)

print("Generated modification:")
print(new_content)

print("\n--- DIFF ---\n")

diff = create_diff(
    file_path,
    old_content,
    new_content
)

print(diff)
