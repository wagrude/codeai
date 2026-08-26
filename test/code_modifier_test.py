from src.editor import create_diff, apply_change
import ollama


def generate_modified_content(old_content, instruction):

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


instruction = "Change the add function so it returns a + b + 20."


new_content = generate_modified_content(
    old_content,
    instruction
)


diff = create_diff(
    file_path,
    old_content,
    new_content
)


print("\n--- PROPOSED CHANGE ---\n")
print(diff)

if not diff:
    print("No changes detected.")
    exit(0)


answer = input("\nApply this change? [y/N]: ").strip().lower()


if answer == "y":

    apply_change(
        file_path,
        new_content
    )

    print("\nChange applied.")

else:

    print("\nChange discarded.")