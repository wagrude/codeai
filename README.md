````markdown
# CodeAI

CodeAI is a local command-line coding assistant that analyzes source code using a locally hosted Large Language Model (LLM).

The current version accepts a source-code file from the command line, reads its contents, builds an analysis prompt, sends the prompt to a local Qwen3-Coder 30B model through Ollama, and displays the generated analysis directly in the terminal.

The project is being developed incrementally, starting with basic code analysis and progressing toward a project-aware local coding agent.

---

## Current Status

**Version: V1 — Basic Code Analysis**

V1 is complete and currently supports:

- Command-line file input
- File existence validation
- Source-code reading
- Prompt generation
- Local LLM communication through Ollama
- Code analysis and review
- Terminal output

### Current Flow

```text
Source File
    |
    v
CodeAI CLI
    |
    v
File Validation
    |
    v
Read Source Code
    |
    v
Build Analysis Prompt
    |
    v
Ollama
    |
    v
Qwen3-Coder 30B
    |
    v
Receive Response
    |
    v
Display Analysis
````

---

# Features

## V1

* Accept a source file through the command line
* Validate the provided file path
* Read source-code files
* Generate an analysis prompt
* Send the prompt to a local LLM
* Receive the model response
* Display the analysis in the terminal

The current analysis covers:

* What the code does
* Potential bugs
* Memory and safety issues
* Possible improvements

---

# Requirements

* Linux
* Python 3
* Git
* Ollama
* Qwen3-Coder 30B
* GitHub

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

Check Ollama:

```bash
ollama --version
```

Check installed Ollama models:

```bash
ollama list
```

The current model used by CodeAI is:

```text
qwen3-coder:30b
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd codeai
```

---

## 2. Create a Python Virtual Environment

Create the virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Verify Python:

```bash
which python
```

The Python executable should point to the active virtual environment.

---

## 3. Install the Ollama Python Client

Install the dependency:

```bash
python -m pip install ollama
```

Verify the installation:

```bash
python -m pip show ollama
```

The virtual environment should remain active while running CodeAI.

---

# Ollama Setup

CodeAI uses Ollama as the local LLM runtime.

The current model is:

```text
qwen3-coder:30b
```

Check available models:

```bash
ollama list
```

The model can also be tested directly:

```bash
ollama run qwen3-coder:30b
```

The communication flow is:

```text
CodeAI
   |
   v
Ollama Python Client
   |
   v
Ollama
   |
   v
Qwen3-Coder 30B
```

The model runs locally on the machine.

---

# Project Structure

```text
codeai/
|
├── src/
│   └── main.py
|
├── test/
│   └── sample.c
|
├── README.md
├── .gitignore
└── LICENSE
```

### `src/main.py`

The main application entry point.

It currently handles:

* Command-line arguments
* File validation
* File reading
* Prompt creation
* Communication with Ollama
* Displaying the LLM response

### `test/sample.c`

A small C source file used to test the CodeAI pipeline.

### `README.md`

Project documentation.

### `.gitignore`

Specifies files and directories that should not be tracked by Git.

### `LICENSE`

Contains the MIT License.

---

# Running CodeAI

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run CodeAI with a source file:

```bash
python src/main.py test/sample.c
```

The application reads the source file, builds an analysis prompt, sends it to the local Qwen3-Coder 30B model through Ollama, and displays the generated response in the terminal.

---

# Example

The current `test/sample.c` can contain:

```c
#include <stdio.h>

int main() {
    printf("Hello from CodeAI\n");
    return 0;
}
```

Run:

```bash
python src/main.py test/sample.c
```

The execution flow is:

```text
python src/main.py test/sample.c
              |
              v
       Read sample.c
              |
              v
       Extract source code
              |
              v
       Build analysis prompt
              |
              v
            Ollama
              |
              v
       Qwen3-Coder 30B
              |
              v
       Receive response
              |
              v
        Print response
```

The model generates an analysis covering:

* What the code does
* Potential bugs
* Memory and safety issues
* Possible improvements

The exact response depends on the locally hosted model.

---

# Analysis Prompt

The current V1 prompt asks the model to:

1. Explain what the code does.
2. Identify potential bugs.
3. Identify potential memory or safety issues.
4. Suggest possible improvements.

Conceptually, the prompt contains:

```text
Instructions
     +
Source Code
     |
     v
Analysis Prompt
```

The generated prompt is sent to the local Qwen3-Coder 30B model through Ollama.

---

# Architecture

## V1 Architecture

```text
                         User
                          |
                          | CLI command
                          v
                  +----------------+
                  |    CodeAI CLI  |
                  +-------+--------+
                          |
                          | File path
                          v
                  +----------------+
                  |  File Reader   |
                  +-------+--------+
                          |
                          | Source code
                          v
                  +----------------+
                  | Prompt Builder |
                  +-------+--------+
                          |
                          | Prompt
                          v
                  +----------------+
                  |     Ollama     |
                  +-------+--------+
                          |
                          | Model request
                          v
                  +----------------+
                  | Qwen3-Coder 30B|
                  +-------+--------+
                          |
                          | Response
                          v
                  +----------------+
                  | Terminal Output|
                  +----------------+
```

---

# Component Responsibilities

## CLI

The CLI accepts the source-code file path.

Example:

```bash
python src/main.py test/sample.c
```

The file path is received through command-line arguments.

---

## File Validation

CodeAI checks whether the supplied path points to an existing file.

Example:

```bash
python src/main.py test/missing.c
```

Expected output:

```text
Error: File not found: test/missing.c
```

---

## File Reader

The file reader:

1. Opens the source file.
2. Reads its contents.
3. Stores the source code.
4. Passes the source code to the prompt builder.

Flow:

```text
Source File
     |
     v
File Reader
     |
     v
Source Code
```

---

## Prompt Builder

The source code is combined with the analysis instructions.

```text
Instructions
     +
Source Code
     |
     v
Analysis Prompt
```

---

## Local LLM

CodeAI communicates with the locally hosted Qwen3-Coder 30B model through Ollama.

```text
CodeAI
   |
   v
Ollama Python Client
   |
   v
Ollama
   |
   v
Qwen3-Coder 30B
```

---

## Terminal Output

The generated response is displayed directly in the terminal.

```text
Source File
    |
    v
Analysis
    |
    v
Terminal
```

---

# V1 Implementation Checklist

* [x] Create project structure
* [x] Create Python entry point
* [x] Accept command-line arguments
* [x] Validate file path
* [x] Read source file
* [x] Handle file errors
* [x] Build analysis prompt
* [x] Connect to local LLM
* [x] Send request
* [x] Receive response
* [x] Display response

### Complete V1 Pipeline

```text
File
 |
 v
Read
 |
 v
Prompt
 |
 v
Ollama
 |
 v
Qwen3-Coder
 |
 v
Response
 |
 v
Terminal
```

---

# Roadmap

## V2 — Multiple Analysis Commands

The next version will introduce different analysis modes.

Planned commands:

```bash
python src/main.py explain test/sample.c
```

```bash
python src/main.py review test/sample.c
```

```bash
python src/main.py debug test/sample.c
```

Possible commands:

```text
explain
review
debug
```

### Explain

```text
explain
   |
   v
Explain code structure and behavior
```

### Review

```text
review
   |
   v
Find bugs, risks, and improvements
```

### Debug

```text
debug
   |
   v
Analyze errors and possible causes
```

---

# V3 — Project Context

Instead of analyzing only one file, CodeAI will eventually be able to inspect an entire project.

Example:

```text
project/
|
├── src/
│   ├── main.c
│   ├── hash_table.c
│   └── hash_table.h
|
├── tests/
│   └── test_hash.c
|
└── README.md
```

Planned flow:

```text
Project Directory
       |
       v
File Discovery
       |
       v
Relevant Files
       |
       v
Context Builder
       |
       v
Local LLM
       |
       v
Analysis
```

---

# V4 — Compiler Integration

A future version will allow CodeAI to compile source code and analyze compiler output.

Planned flow:

```text
Source Code
     |
     v
Compiler
     |
     +--------------------+
     |                    |
     v                    v
  Success                Error
                          |
                          v
                  Compiler Output
                          |
                          v
                      Local LLM
                          |
                          v
                       Analysis
```

For C and C++ projects, compilers such as GCC and Clang can be integrated.

---

# V5 — Tool Calling

A future version can allow the model to request controlled tools.

Potential tools:

```text
read_file()
list_files()
search_code()
compile_code()
run_test()
```

Planned architecture:

```text
                       Local LLM
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        read_file()   search_code()  compile_code()
             |             |             |
             +-------------+-------------+
                           |
                           v
                         Result
                           |
                           v
                       Local LLM
```

Tools will be explicitly controlled by the application.

---

# V6 — Safe Code Modification

A future version can allow CodeAI to generate changes to source files.

Planned workflow:

```text
Read Code
    |
    v
Analyze
    |
    v
Generate Change
    |
    v
Show Change to User
    |
    v
User Approval
    |
    v
Modify File
    |
    v
Compile / Test
```

The application should not automatically modify files without user approval.

---

# V7 — Local Coding Agent

The long-term goal is to evolve CodeAI into a project-aware local coding agent.

Planned architecture:

```text
                         User
                          |
                          v
                  +----------------+
                  |    CodeAI      |
                  |     Agent      |
                  +-------+--------+
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
     File System       Compiler        Search
          |               |               |
          +---------------+---------------+
                          |
                          v
                      Local LLM
                          |
                          v
                       Decision
                          |
                          v
                       Tool Call
                          |
                          v
                         Result
                          |
                          v
                      Local LLM
                          |
                          v
                       Response
```

The agent can eventually:

* Understand project structure
* Read relevant files
* Search source code
* Analyze compiler errors
* Run controlled tests
* Explain problems
* Suggest changes
* Apply approved changes
* Verify the result

---

# Error Handling

## Missing File

```bash
python src/main.py test/missing.c
```

Expected output:

```text
Error: File not found: test/missing.c
```

## Missing Command-Line Argument

```bash
python src/main.py
```

Expected output:

```text
Usage: python src/main.py <file>
```

## Empty File

Empty-file handling is planned for a future version.

## Local LLM Unavailable

Future versions will provide a clear error message if the Ollama service is unavailable.

---

# Security Considerations

The current version only reads source files and sends their contents to the locally hosted model.

Future versions will require additional security controls when CodeAI gains the ability to execute commands or modify files.

Planned controls include:

* User confirmation before file modification
* Restricted command execution
* Command allowlists
* Sandboxed execution
* Restricted working directories
* Protection against destructive commands
* Controlled tool permissions

CodeAI should never blindly execute commands generated by an LLM.

---

# Testing

The current testing process uses small source-code files.

Initial test directory:

```text
test/
└── sample.c
```

Run:

```bash
python src/main.py test/sample.c
```

Future testing will cover:

```text
Valid source files
Missing files
Empty files
Large files
Invalid source code
Compiler errors
Multiple source files
LLM connection failures
Malformed responses
```

Future versions can introduce automated tests for individual components.

---

# Git Workflow

Development is organized around logical changes.

Each meaningful implementation step is committed separately.

Check repository status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Add <description>"
```

Push changes:

```bash
git push
```

View commit history:

```bash
git log --oneline
```

Example commit messages:

```text
Initialize CodeAI project
Add CLI file input
Add file validation
Add source file reader
Add prompt generation
Integrate Ollama
Add local code analysis
```

Example:

```bash
git add .
git commit -m "Integrate Ollama"
git push
```

---

# Development Commands

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

Check Ollama:

```bash
ollama --version
```

List Ollama models:

```bash
ollama list
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the Ollama Python client:

```bash
python -m pip install ollama
```

Run CodeAI:

```bash
python src/main.py test/sample.c
```

Check Git status:

```bash
git status
```

View commit history:

```bash
git log --oneline
```

---

# Planned Project Structure

As the project grows, the structure can evolve into:

```text
codeai/
|
├── src/
│   ├── main.py
│   ├── cli.py
│   ├── file_reader.py
│   ├── prompt.py
│   ├── llm.py
│   ├── tools.py
│   └── agent.py
|
├── test/
│   ├── sample.c
│   └── ...
|
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

Additional modules will only be introduced when their functionality is required.

---

# Development Roadmap

```text
V1
Basic Code Analysis
        |
        v
V2
Multiple Analysis Commands
        |
        v
V3
Project Context
        |
        v
V4
Compiler Integration
        |
        v
V5
Tool Calling
        |
        v
V6
Safe Code Modification
        |
        v
V7
Local Coding Agent
```

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

```
```
