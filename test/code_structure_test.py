from src.code_structure import CodeStructure


source = """
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(10, 20);
    printf("%d\\n", result);
    return 0;
}
"""


analyzer = CodeStructure()

result = analyzer.analyze(source)

print("Functions:")

for function in result["functions"]:

    print(f"\n  Name: {function['name']}")
    print(f"  Return type: {function['return_type']}")
    print("  Parameters:")

    for parameter in function["parameters"]:
        print(
            f"    {parameter['type']} "
            f"{parameter['name']}"
        )

    print(
        f"  Lines: "
        f"{function['start_line']}-"
        f"{function['end_line']}"
    )