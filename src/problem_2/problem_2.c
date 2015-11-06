#include <stdio.h>

/*
 * Solution to problem 2
 *
 * https://projecteuler.net/problem=2
 */

int main(void) {
    int solution = fibonacci();
    printf("%i", solution);
}

int fibonacci(void) {
    int limit = 4000000;
    int a = 1;
    int b = 2;
    int sum = 0;
    int c = 0;

    while (b < limit) {
        if (b % 2 == 0) {
            sum = sum + b;
        }
        c = a + b;
        a = b;
        b = c;
    }

    return sum;
}


