#include <stdio.h>

// counts how many 1s in a row start at position i
int runLength(int a[], int n, int i)
{
    int count = 0;

    // keep going until we hit a 0 or the end of the array
    while (i < n && a[i] == 1) {
        count++;
        i++;
    }
    return count;
}

int main()
{
    int n, k, i;

    // read number of entries and the limit k
    printf("Enter n: ");
    scanf("%d", &n);
    printf("Enter k: ");
    scanf("%d", &k);

    // read the activity log (1 = studying, 0 = break)
    int a[n];
    printf("Enter the log: ");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    int ans = 0;   // stays 0 if the rule is never broken

    for (i = 0; i < n; i++) {
        // if the run starting here is longer than k, the rule breaks
        if (runLength(a, n, i) > k) {
            // (k+1)th session of this run is at position i+k,
            // +1 because sessions are numbered from 1
            ans = i + k + 1;
            break;
        }
    }

    printf("%d\n", ans);
    return 0;
}
