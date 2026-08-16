import sys
import os

if len(sys.argv) < 2:
    print("Usage: python src/main.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"Error: File not found: {file_path}")
    sys.exit(1)

with open(file_path, "r") as file:
    code = file.read()

print(code)