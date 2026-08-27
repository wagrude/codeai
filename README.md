<div align="center">

# CodeAI

### A local AI coding assistant that understands your code.

Analyze · Review · Debug · Retrieve

<br>

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![C/C++](https://img.shields.io/badge/C%2FC%2B%2B-Systems-orange)](#)
[![Ollama](https://img.shields.io/badge/AI-Ollama-black)](https://ollama.com/)
[![Local AI](https://img.shields.io/badge/AI-Local-green)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow)](#license)

<br>

**Local AI for understanding, analyzing, and working with codebases.**

</div>

---

## What is CodeAI?

CodeAI is a local AI-powered developer tool designed to understand source code and progressively work with entire codebases.

It provides code analysis, review, debugging, and semantic code retrieval using local AI models.

---

## Current Version

### V3 — Semantic Code Retrieval

CodeAI can currently:

* Analyze source code
* Review code
* Debug code
* Scan repositories
* Chunk source code
* Generate local embeddings
* Perform semantic similarity search
* Retrieve relevant code

---

## Architecture

```text
Repository
    │
    ▼
  Scanner
    │
    ▼
  Chunker
    │
    ▼
Local Embeddings
    │
    ▼
Vector Store
    │
    ▼
Similarity Search
    │
    ▼
Relevant Code
    │
    ▼
Local LLM
```

---

## Tech Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Language          | Python                |
| Systems           | C / C++               |
| LLM Runtime       | Ollama                |
| Coding Model      | Qwen3-Coder 30B       |
| Embeddings        | nomic-embed-text      |
| Vector Operations | NumPy                 |
| Platform          | Linux                 |
| AI                | Local / Offline-first |

---

## Usage

### Explain

```bash
python src/main.py explain test/sample.c
```

### Review

```bash
python src/main.py review test/sample.c
```

### Debug

```bash
python src/main.py debug test/sample.c
```

---

## Future Versions

### V4

Compiler integration and compiler-aware debugging.

### V5

Controlled tool calling and development tools.

### V6

Safe file creation and code modification.

### V7

Project-aware coding agent with conversation context.

### V8

Sandboxing, advanced execution, and scalable architecture.

### V9+

Multimodal development support and further agent capabilities.

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

<div align="center">

### CodeAI

**Local AI · Code Understanding · Developer Tools**

</div>