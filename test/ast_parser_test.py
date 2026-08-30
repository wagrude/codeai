
from src.ast_parser import CParser


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


parser = CParser()

tree = parser.parse(source)

print(tree.root_node)
