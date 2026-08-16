import sys
import os
import ollama

if len(sys.argv) < 2:
    print("Usage: python src/main.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"Error: File not found: {file_path}")
    sys.exit(1)

with open(file_path, "r") as file:
    code = file.read()

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