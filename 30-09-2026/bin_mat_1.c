/*Code by Nethra Gu[ta
 * 30-09-2026
 * Random n x m binary matrix.
 * From github.com/gadepall/ncert-probability:
 *   createMat() - codes/coeffs-mat.h
 *   bernoulli() - ncert/11/16/3/8/codes/binomial.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "coeffs-mat.h"

// from the repo: returns 1 with probability p
int bernoulli(double p) {
    double s = (double)rand()/RAND_MAX;
    return (s <= p)?1:0;
}

int main() {
    srand(time(NULL));

    int n, m;
    scanf("%d %d", &n, &m);

    double **a = createMat(n, m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = bernoulli(0.5);

    printf("%d %d\n", n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (j > 0) printf(" ");
            printf("%d", (int)a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
