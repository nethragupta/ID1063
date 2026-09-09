#include <stdio.h>
int main()
{
	char a[50];
	printf("Enter a word:");
	scanf("%s", a);
	int length = strlen(a);
	int t=0;
	for (int i = 0; i < length; i++)
		if (a[i] != a[length-1-i])
		{t = 1;
			break;
		}
if (t==0)
	printf("Palindrome");
else
printf("Not a Palindrome");
			
return 0;
}
