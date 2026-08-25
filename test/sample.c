#include <stdio.h>
#include <stdlib.h>

int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

void print_result(int value) {
    printf("Result: %d\n", value);
}

int main() {
    int x = 10;
    int y = 20;

    int sum = add(x, y);
    int product = multiply(x, y);

    print_result(sum);
    print_result(product);

    return 0;
}