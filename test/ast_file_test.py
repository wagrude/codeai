from src.code_structure import CodeStructure


FILE = "test/benchmark_large/main.c"


with open(FILE, "r", encoding="utf-8") as file:
    source = file.read()


analyzer = CodeStructure()
result = analyzer.analyze(source)


print(f"File: {FILE}")

print("\nIncludes:")
for item in result["includes"]:
    print(
        f"  {item['content'].strip()} "
        f"(lines {item['start_line']}-{item['end_line']})"
    )

print("\nFunctions:")
for item in result["functions"]:
    print(
        f"  {item['name']} "
        f"(lines {item['start_line']}-{item['end_line']})"
    )

print("\nCalls:")
for item in result["calls"]:
    print(
        f"  {item['name']} "
        f"(lines {item['start_line']}-{item['end_line']})"
    )