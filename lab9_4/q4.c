#include <stdio.h>
#include <math.h>

// returns first i where |a[i+1]-a[i]| <= tol, else -1
int firstStable(double a[], int n, double tol)
{
    int i;
    for (i = 0; i < n-1; i++)
        if (fabs(a[i+1]-a[i]) <= tol + 1e-9)   // difference small enough
            return i;
    return -1;   // never got within tolerance
}

int main()
{
    int n, i;
    double tol;
    printf("Enter n: ");
    scanf("%d", &n);
    double a[n];
    printf("Enter the readings: ");
    for (i = 0; i < n; i++)
        scanf("%lf", &a[i]);
    printf("Enter tolerance: ");
    scanf("%lf", &tol);
    printf("%d\n", firstStable(a, n, tol));
    return 0;
}
