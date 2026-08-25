def chunk_file(file_path, chunk_size=80, overlap=10):

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    with open(file_path, "r") as file:
        lines = file.readlines()

    chunks = []

    start = 0

    while start < len(lines):
        end = min(start + chunk_size, len(lines))

        chunk = {
            "file": file_path,
            "start_line": start + 1,
            "end_line": end,
            "content": "".join(lines[start:end])
        }

        chunks.append(chunk)

        if end == len(lines):
            break

        start = end - overlap

    return chunks

if __name__ == "__main__":
    chunks = chunk_file("test/sample.c", chunk_size=10, overlap=2)

    for chunk in chunks:
        print(
            f"\n--- {chunk['start_line']}-{chunk['end_line']} ---"
        )
        print(chunk["content"])