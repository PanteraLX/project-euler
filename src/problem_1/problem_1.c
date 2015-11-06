#include <stdio.h>

/*
 * Solution to problem 1
 *
 * https://projecteuler.net/problem=1
 */


int main(void)
{
    int solution = run();
    printf("%i", solution);
}

int run()
{
    int sum = 0;
    int ii;
    for (ii = 0; ii < 1000; ii++) {
        if (ii % 3 == 0 || ii % 5 == 0)
            sum += ii;
    }
    return sum;
}

