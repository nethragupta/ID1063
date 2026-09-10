#include <stdio.h>
#include <math.h>

// Function f(x) = e^x - 2
double f(double x) {
    return exp(x) - 2.0;
}

// Derivative f'(x) = e^x
double df(double x) {
    return exp(x);
}

int main() {
    double x = 1.0;          // Initial guess x0 = 1
    double x_next;
    double tolerance = 1e-9; // Target precision
    int max_iterations = 10;

    printf("Iter |      x_n      |    f(x_n)    \n");
    printf("----------------------------------\n");
    printf("%4d | %13.9f | %12.9f\n", 0, x, f(x));

    for (int i = 1; i <= max_iterations; i++) {
        // Newton-Raphson update step
        x_next = x - (f(x) / df(x));
        
        printf("%4d | %13.9f | %12.9f\n", i, x_next, f(x_next));

        // Check if converged
        if (fabs(x_next - x) < tolerance) {
            printf("----------------------------------\n");
            printf("Converged to exact root: %.9f\n", x_next);
            printf("Theoretical exact (ln 2): %.9f\n", log(2.0));
            return 0;
        }

        x = x_next;
    }

    return 0;
}

