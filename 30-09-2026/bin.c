/*Code by Nethra Gupta
 * 30-09-2026
 * Code to generate a random binary vector of size n.
 * The bernoulli() function is taken from the
  ncert-probability repo (github.com/gadepall/ncert-probability),
 * file: ncert/11/16/3/8/codes/binomial.c
 * main() is my own code, written to call bernoulli() n times.
 */

#include <stdio.h>  
#include <stdlib.h> 
#include <time.h>   

// ---- From the repo (binomial.c) ----
// Returns 1 with probability p, and 0 otherwise
int bernoulli(double p) {
    double s = (double)rand()/RAND_MAX;

    return (s <= p)?1:0;
}
// ---- End of code from the repo ----

int main() {
    // seed with the current time so each run gives a different vector
    srand(time(NULL));

    int n;
    scanf("%d", &n);   // read the size of the vector

    // print n random bits, each 1 with probability 0.5
    for (int i = 0; i < n; i++)
        printf("%d ", bernoulli(0.5));

    printf("\n");      // end the line after the vector
    return 0;
}
