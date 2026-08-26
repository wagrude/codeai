import sys
import os
import ollama

from src.codeai import CodeAI


if len(sys.argv) < 3:
    print("Usage:")
    print("  python src/main.py <command> <file>")
    print('  python src/main.py ask <project> "<question>"')
    print("  python src/main.py chat <project>")
    print('  python src/main.py modify <file> "<instruction>"')
    print('  python src/main.py create <file> "<instruction>"')
    sys.exit(1)


command = sys.argv[1]


# --------------------------------------------------
# Repository-aware single question
# --------------------------------------------------

if command == "ask":

    if len(sys.argv) < 4:
        print('Usage: python src/main.py ask <project> "<question>"')
        sys.exit(1)

    project_path = sys.argv[2]
    question = sys.argv[3]

    if not os.path.isdir(project_path):
        print(f"Error: Project directory not found: {project_path}")
        sys.exit(1)

    codeai = CodeAI(project_path)

    response = codeai.ask(question)

    print(response)

    sys.exit(0)


# --------------------------------------------------
# Interactive repository chat
# --------------------------------------------------

if command == "chat":

    project_path = sys.argv[2]

    if not os.path.isdir(project_path):
        print(f"Error: Project directory not found: {project_path}")
        sys.exit(1)

    codeai = CodeAI(project_path)

    print("CodeAI interactive mode")
    print("Type 'exit' or 'quit' to leave.\n")

    while True:

        try:
            question = input("CodeAI> ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        if not question:
            continue

        answer = codeai.ask(question)

        print("\n" + answer + "\n")

    sys.exit(0)


# --------------------------------------------------
# Repository-aware modification
# --------------------------------------------------

if command == "modify":

    if len(sys.argv) < 4:
        print('Usage: python src/main.py modify <file> "<instruction>"')
        sys.exit(1)

    file_path = sys.argv[2]
    instruction = sys.argv[3]

    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    codeai = CodeAI(".")

    codeai.modify(
        file_path,
        instruction
    )

    sys.exit(0)


# --------------------------------------------------
# Repository-aware file creation
# --------------------------------------------------

if command == "create":

    if len(sys.argv) < 4:
        print('Usage: python src/main.py create <file> "<instruction>"')
        sys.exit(1)

    file_path = sys.argv[2]
    instruction = sys.argv[3]

    if os.path.exists(file_path):
        print(f"Error: File already exists: {file_path}")
        sys.exit(1)

    codeai = CodeAI(".")

    codeai.create(
        file_path,
        instruction
    )

    sys.exit(0)


# --------------------------------------------------
# Existing file-based commands
# --------------------------------------------------

file_path = sys.argv[2]

if not os.path.isfile(file_path):
    print(f"Error: File not found: {file_path}")
    sys.exit(1)


with open(file_path, "r") as file:
    code = file.read()


if command == "explain":

    prompt = f"""
Explain the following source code in simple terms.

Cover:
1. What the code does.
2. How the main parts work.
3. The overall flow of the program.

Source code:

{code}
"""


elif command == "review":

    prompt = f"""
Review the following source code.

Explain:
1. What the code does.
2. Potential bugs.
3. Potential memory or safety issues.
4. Possible improvements.

Source code:

{code}
"""


elif command == "debug":

    prompt = f"""
Debug the following source code.

Explain:
1. What the code is supposed to do.
2. What errors or problems may exist.
3. Why those problems occur.
4. How to fix them.

Source code:

{code}
"""


else:

    print(f"Unknown command: {command}")

    print(
        "Available commands: "
        "explain, review, debug, ask, chat, modify, create"
    )

    sys.exit(1)


response = ollama.chat(
    model="qwen3-coder:30b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])