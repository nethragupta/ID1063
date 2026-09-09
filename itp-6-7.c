#include <stdio.h>

void replace_char(char a[], char x, char y)
{
    for (int i = 0;i<strlen(a); i++)
    {
//if the letter is x, replace it with y
        if (a[i] == x)
	{
            a[i] = y;
        }
    }
}
//taking inputs
int main() {
    char str[100];
    char x, y;
    printf("Enter a string: \n");
    scanf("%s", str);
    printf("Enter a character in the string:\n");
    scanf(" %c", &x);
    printf("Enter the character you want to replace it with:\n");
    scanf(" %c", &y);
//calling the function
    replace_char(str, x, y);

    printf("%s\n", str);

    return 0;
}


