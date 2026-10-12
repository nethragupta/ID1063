/* 4-bit Johnson counter (GATE 2025 CS Q.60)
 * D0 = NOT Q3, D1 = Q0, D2 = Q1, D3 = Q2
 * Prints each state until the counter returns to the initial state.
 */
#include <stdio.h>

#define N 4

void print_state(int q[], int tick)
{
    printf("Tick %d: ", tick);
    for (int i = 0; i < N; i++)
        printf("%d", q[i]);          /* order: Q0 Q1 Q2 Q3 */
    printf("\n");
}

int same(int a[], int b[])
{
    for (int i = 0; i < N; i++)
        if (a[i] != b[i])
            return 0;
    return 1;
}

int main(void)
{
    int q[N], start[N], d[N];

    printf("Enter initial state Q0 Q1 Q2 Q3 (e.g. 0 0 0 0): ");
    for (int i = 0; i < N; i++) {
        if (scanf("%d", &q[i]) != 1 || (q[i] != 0 && q[i] != 1)) {
            printf("Each bit must be 0 or 1.\n");
            return 1;
        }
        start[i] = q[i];
    }

    int tick = 0;
    print_state(q, tick);

    do {
        /* compute all D inputs first (all flip-flops clock together) */
        d[0] = !q[N - 1];            /* D0 = Q3' */
        for (int i = 1; i < N; i++)
            d[i] = q[i - 1];         /* Di = Q(i-1) */

        /* clock edge: Q <- D */
        for (int i = 0; i < N; i++)
            q[i] = d[i];

        tick++;
        print_state(q, tick);
    } while (!same(q, start));

    printf("Number of distinct states: %d\n", tick);
    return 0;
}

