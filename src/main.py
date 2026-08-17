import sys
import os
import ollama

if len(sys.argv) < 3:
    print("Usage: python src/main.py <command> <file>")
    sys.exit(1)

command = sys.argv[1]
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
    print("Available commands: explain, review, debug")
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