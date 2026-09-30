/*
 * Q7: Cursed treasure chest, with a random test array.
 * Code from github.com/gadepall:
 *   min()          - cprog, codes/data/minmax.c (changed to return a pointer)
 *   random numbers - ncert-probability, codes/coeffs.h, uniform()
 *   malloc array   - cprog, codes/prog/fileprogs/pointer.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// from cprog minmax.c, changed to return a pointer to the smallest
// element instead of its value
int *min(int *a, int n){
int *temp=&a[0];
  for (int i = 1; i < n; i++){
	  if(*temp > a[i])
		  temp = &a[i];
  }
  return temp;
}

int main() {
    srand(time(NULL));

    int n;
    printf("Enter number of chests: ");
    scanf("%d", &n);

    // array of n chests, same malloc style as pointer.c
    int *a = (int *)malloc(n * sizeof(*a));

    // uniform random coins from 1 to 100, based on uniform() in coeffs.h
    for (int i = 0; i < n; i++)
        a[i] = 1 + (int)((double)rand()/((double)RAND_MAX + 1) * 100);

    printf("Test array:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");

    // pointer to the cursed chest, then empty it through the pointer
    int *cursed = min(a, n);
    *cursed = 0;

    printf("Updated array:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    printf("\n");

    free(a);
    return 0;
}
