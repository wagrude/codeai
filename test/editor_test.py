from src.editor import create_diff, apply_change


file_path = "test/edit_target.c"

old_content = """int add(int a, int b) {
    return a + b;
}
"""

new_content = """int add(int a, int b) {
    return a + b + 1;
}
"""

diff = create_diff(
    file_path,
    old_content,
    new_content
)

print("Generated diff:")
print(diff)

apply_change(
    file_path,
    new_content
)

print("Change applied.")

with open(file_path, "r", encoding="utf-8") as file:
    result = file.read()

print("Final file:")
print(result)