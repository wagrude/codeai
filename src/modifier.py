import ollama

from src.editor import create_diff, apply_change


MODEL = "qwen3-coder:30b"


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
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def propose_change(file_path, instruction):
    with open(file_path, "r", encoding="utf-8") as file:
        old_content = file.read()

    new_content = generate_modified_content(
        old_content,
        instruction
    )

    diff = create_diff(
        file_path,
        old_content,
        new_content
    )

    return old_content, new_content, diff


def apply_proposed_change(
    file_path,
    old_content,
    new_content,
    diff
):
    if not diff:
        return False

    print("\n--- PROPOSED CHANGE ---\n")
    print(diff)

    answer = input("\nApply this change? [y/N]: ").strip().lower()

    if answer != "y":
        print("\nChange discarded.")
        return False

    apply_change(
        file_path,
        new_content
    )

    print("\nChange applied.")
    return True
