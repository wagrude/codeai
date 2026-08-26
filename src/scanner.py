import os

SUPPORTED_EXTENSIONS = {
    ".c",
    ".h",
    ".cpp",
    ".hpp",
    ".py",
    ".js",
    ".ts",
    ".java"
}
IGNORED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "test"
}

def scan_project(path):
    files_found = []

    for root, dirs, files in os.walk(path):
        dirs[:] = [
            directory
            for directory in dirs
            if directory not in IGNORED_DIRS
        ]

        for file in files:
            extension = os.path.splitext(file)[1].lower()

            if extension not in SUPPORTED_EXTENSIONS:
                continue

            file_path = os.path.join(root, file)
            files_found.append(file_path)

    return files_found


if __name__ == "__main__":
    files = scan_project(".")
    
    for file in files:
        print(file)