#include "math.h"
#include "utils.h"

int main() {
    int x = 10;
    int y = 20;

    int sum = add(x, y);
    int product = multiply(x, y);

    print_result("Sum", sum);
    print_result("Product", product);

    return 0;
}
