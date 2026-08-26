from src.editor import create_diff


old_content = """int add(int a, int b) {
    return a + b;
}
"""

new_content = """int add(int a, int b) {
    return a + b + 1;
}
"""

diff = create_diff(
    "test/sample.c",
    old_content,
    new_content
)

print(diff)
