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