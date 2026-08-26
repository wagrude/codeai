import difflib


def create_diff(file_path, old_content, new_content):
    diff = difflib.unified_diff(
        old_content.splitlines(keepends=True),
        new_content.splitlines(keepends=True),
        fromfile=file_path,
        tofile=file_path,
    )

    return "".join(diff)
