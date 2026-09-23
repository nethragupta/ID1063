#include <stdio.h>

int runLength(int a[], int n, int i)
{
    int count = 0;

    while (i < n && a[i] == 1) {
        count++;
        i++;
    }
    return count;
}

int main()
{
    int n, k, i;
    scanf("%d %d", &n, &k);

    int a[n];
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);

    int ans = 0;
    for (i = 0; i < n; i++) {
        if (runLength(a, n, i) > k) {
            ans = i + k + 1;
            break;
        }
    }

    printf("%d\n", ans);
    return 0;
}
