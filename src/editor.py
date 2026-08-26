import difflib


def create_diff(file_path, old_content, new_content):
    diff = difflib.unified_diff(
        old_content.splitlines(keepends=True),
        new_content.splitlines(keepends=True),
        fromfile=file_path,
        tofile=file_path,
    )

    return "".join(diff)


def apply_change(file_path, new_content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)