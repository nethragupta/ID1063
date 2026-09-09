#include <stdio.h>
int main()
{
	char a[50];
	char b;
	printf("Input:");
	scanf("%s", a);
	printf("character:");
	scanf(" %c", &b);
	int t = -1;
for (int i = 0; i<50; i++)
{
	if (a[i] == b)
	{
		t = i;
		break;
	}
}
	printf("%d", t);
return 0;
}
