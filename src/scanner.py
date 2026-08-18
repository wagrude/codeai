import os

IGNORED_DIRS = {".git", ".venv", "__pycache__"}

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

def scan_project(path):
    files_found = []

    for root, dirs, files in os.walk(path):
        dirs[:] = [directory for directory in dirs if directory not in IGNORED_DIRS]

        for file in files:
            file_path = os.path.join(root, file)
            files_found.append(file_path)

    return files_found


files = scan_project(".")
print(files)