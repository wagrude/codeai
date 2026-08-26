from src.file_creator import (
    propose_file,
    apply_file
)


file_path = "test/generated_list.c"

instruction = """
Create a complete singly linked list implementation.

Include:
- Node structure
- Function to create a node
- Function to insert at the beginning
- Function to print the list
- main() demonstrating the implementation
"""


content = propose_file(
    file_path,
    instruction
)

print("\n--- PROPOSED FILE ---\n")
print(content)

answer = input("\nCreate this file? [y/N]: ").strip().lower()


if answer == "y":

    apply_file(
        file_path,
        content
    )

    print(f"\nFile created: {file_path}")

else:

    print("\nFile creation discarded.")
