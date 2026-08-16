import sys

file_path = sys.argv[1]

with open(file_path, "r") as file:
    code = file.read()

print(code)