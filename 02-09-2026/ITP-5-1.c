#include <stdio.h>
int main()
{
	int n;
	printf("Enter an  positive integer n: ");
	scanf("%d", &n);
	int arr[n];
	for (int i = 0; i<n; i+=1)
	{
		arr[i] = i + 1;
	}
	for (int j=0; j<n; j+=1)
	{
		for (int i = 0; i<n; i+=1)
		{	
	printf(" %d", (j+1) * arr[i]);
		}
	printf("\n");
	}
	return 0;
}