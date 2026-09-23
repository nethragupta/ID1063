#include <stdio.h>

int days_elapsed(int d,int m)
{
    int days[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int t =0;
    for (int i  0; i <m  - 1;i++)
        t = t+days[i];

    return t + d;
}

int main()
{
    int d, m;
    scanf("%d %d", &d, &m);
    printf("%d\n",days_elapsed(d, m));
    return 0;
}
