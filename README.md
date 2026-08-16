# CodeAI

CodeAI is a local command-line coding assistant that uses a locally hosted Large Language Model (LLM) to analyze source code. The project is designed to progressively evolve from a simple file-based code reviewer into a project-aware coding agent capable of inspecting source files, analyzing compiler errors, using development tools, and assisting with code modifications.

The first version focuses on a simple and well-defined pipeline:

```text
Source File
    |
    v
CodeAI CLI
    |
    v
Read Source Code
    |
    v
Build Prompt
    |
    v
Local LLM
    |
    v
Receive Response
    |
    v
Display Result
```

The application is designed to work locally so that source code does not need to be sent to an external cloud AI service.

---

## Project Status

Current version: **V1 - Basic Code Analysis**

V1 is focused on implementing the following functionality:

```text
File Path
   |
   v
Validate File
   |
   v
Read File
   |
   v
Create Prompt
   |
   v
Send to Local LLM
   |
   v
Receive Response
   |
   v
Print Response
```

The following features are planned for later versions:

- Multiple analysis commands
- Code explanation
- Code review
- Project-level context
- Multiple file analysis
- Compiler integration
- Error analysis
- Tool calling
- Controlled command execution
- Safe file modification
- Automated testing
- Local project memory

---

# Requirements

The current development environment uses:

- Linux
- Python 3
- Git
- A locally hosted LLM
- GitHub

Python version can be checked with:

```bash
python3 --version
```

Git can be checked with:

```bash
git --version
```

The local LLM runtime must expose a local API that CodeAI can communicate with.

---

# Installation

## 1. Clone the repository

Clone the repository using Git:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd codeai
```

Verify the repository:

```bash
ls
```

---

## 2. Create the project directories

Create the source and test directories:

```bash
mkdir -p src test
```

Create the initial files:

```bash
touch src/main.py
touch test/sample.c
```

The project structure should now be:

```text
codeai/
├── src/
│   └── main.py
├── test/
│   └── sample.c
├── README.md
├── .gitignore
└── LICENSE
```

---

# Running the Current Version

The initial application can be started with:

```bash
python3 src/main.py
```

As development progresses, the intended command-line interface will be:

```bash
python3 src/main.py <file>
```

For example:

```bash
python3 src/main.py test/sample.c
```

The program will read the specified source file and pass its contents to the configured local LLM for analysis.

---

# Example Source File

The initial test file can contain:

```c
#include <stdio.h>

int main() {
    int *ptr = NULL;

    printf("%d", *ptr);

    return 0;
}
```

The intended V1 execution flow is:

```text
python3 src/main.py test/sample.c
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
         Local LLM
              |
              v
       Receive response
              |
              v
        Print response
```

A response may contain information such as:

```text
Explanation:
The program attempts to dereference a NULL pointer.

Problem:
The pointer does not point to a valid memory location.

Potential Result:
Dereferencing the pointer can cause a segmentation fault.

Suggested Improvement:
Initialize the pointer with a valid memory address before
dereferencing it.
```

The exact response depends on the locally hosted model.

---

# Architecture

## V1 Architecture

```text
                         User
                          |
                          | CLI command
                          v
                  +----------------+
                  |    CodeAI CLI   |
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
                  |    Local LLM   |
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

The command-line interface accepts input from the user.

Example:

```bash
python3 src/main.py test/sample.c
```

The CLI extracts the provided file path and passes it to the application.

---

## File Reader

The file reader is responsible for:

1. Checking whether the file exists.
2. Opening the file.
3. Reading its contents.
4. Handling file-related errors.
5. Returning the source code to the application.

Example:

```text
test/sample.c
     |
     v
File Reader
     |
     v
Source Code
```

---

## Prompt Builder

The source code is combined with instructions for the LLM.

A basic prompt can contain:

```text
Review the following source code.

Explain:
1. What the code does.
2. Potential bugs.
3. Potential memory or safety issues.
4. Possible improvements.

Source code:
<source code>
```

The prompt is then sent to the local LLM.

---

## Local LLM

The local model receives the prompt and generates an analysis.

The application communicates with the model through its locally available API.

No external cloud model is required for the intended architecture.

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

# Development Roadmap

## V1 — Basic Code Analysis

The first version contains only the fundamental pipeline.

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
Local LLM
 |
 v
Response
 |
 v
Terminal
```

Implementation checklist:

- [ ] Create project structure
- [ ] Create Python entry point
- [ ] Accept command-line arguments
- [ ] Validate file path
- [ ] Read source file
- [ ] Handle file errors
- [ ] Build prompt
- [ ] Connect to local LLM
- [ ] Send request
- [ ] Receive response
- [ ] Display response

---

# V2 — Multiple Commands

The command-line interface can be extended with different operations.

Example:

```bash
python3 src/main.py explain test/sample.c
```

```bash
python3 src/main.py review test/sample.c
```

```bash
python3 src/main.py debug test/sample.c
```

Possible commands:

```text
explain
review
debug
```

Each command can use a different prompt and analysis objective.

---

# V3 — Project Context

Instead of analyzing only one file, CodeAI will be able to understand a project directory.

Example:

```text
project/
├── src/
│   ├── main.c
│   ├── hash_table.c
│   └── hash_table.h
├── tests/
│   └── test_hash.c
└── README.md
```

The application can inspect the project structure and provide relevant files to the model.

The flow becomes:

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

CodeAI can eventually compile source code and provide compiler output to the LLM.

Example:

```text
Source Code
     |
     v
Compiler
     |
     +---- Success
     |
     +---- Error
             |
             v
        Compiler Output
             |
             v
          Local LLM
```

For C code, the system can eventually integrate with tools such as:

```bash
gcc
```

or:

```bash
clang
```

The compiler output can then be analyzed by the local model.

---

# V5 — Tool Calling

The model can eventually request controlled tools instead of only receiving source code.

Possible tools:

```text
read_file()
list_files()
search_code()
compile_code()
run_test()
```

Architecture:

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

Tools must be explicitly controlled by the application.

---

# V6 — Safe Code Modification

A future version can allow the model to suggest or generate changes.

The intended workflow is:

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

The final planned architecture is a project-aware local coding agent.

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
     File System       Compiler       Search
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

- Understand project structure
- Read relevant files
- Search source code
- Analyze compiler errors
- Run controlled tests
- Explain problems
- Suggest changes
- Apply approved changes
- Verify the result

---

# Error Handling

CodeAI should handle common errors gracefully.

## Missing file

```bash
python3 src/main.py test/missing.c
```

Expected behavior:

```text
Error: File not found: test/missing.c
```

---

## Invalid arguments

```bash
python3 src/main.py
```

Expected behavior:

```text
Usage: python3 src/main.py <file>
```

---

## Empty file

The application should detect an empty source file and provide an appropriate message rather than sending an empty request to the model.

---

## LLM unavailable

If the local LLM service is not running:

```text
Error: Local LLM service is unavailable.
```

The application should exit cleanly instead of crashing.

---

# Security Considerations

The initial version only reads source files and sends their contents to the locally hosted model.

Future versions will require additional security controls when they gain the ability to execute commands or modify files.

Planned controls include:

- User confirmation before file modification
- Restricted command execution
- Command allowlists
- Sandboxed execution
- Restricted working directories
- Protection against destructive commands
- Controlled tool permissions

CodeAI should never blindly execute commands generated by an LLM.

---

# Testing

Testing will use small source-code files during development.

Initial test directory:

```text
test/
└── sample.c
```

Future tests will cover:

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

---

# Git Workflow

Check the current repository status:

```bash
git status
```

Add files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initialize CodeAI project"
```

Push changes:

```bash
git push
```

View commit history:

```bash
git log --oneline
```

---

# Development Commands

Check Python:

```bash
python3 --version
```

Run the application:

```bash
python3 src/main.py
```

Run with a source file:

```bash
python3 src/main.py test/sample.c
```

Check Git status:

```bash
git status
```

---

# Planned Project Structure

The initial structure is intentionally small.

As the project grows, it can evolve into:

```text
codeai/
│
├── src/
│   ├── main.py
│   ├── cli.py
│   ├── file_reader.py
│   ├── prompt.py
│   ├── llm.py
│   ├── tools.py
│   └── agent.py
│
├── test/
│   ├── sample.c
│   └── ...
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

The additional modules will only be introduced when their functionality is required.

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.