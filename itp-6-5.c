#include <stdio.h>
#include <string.h>

int main() {
    char a[50];
    printf("Enter a phrase: ");
    fgets(a, sizeof(a), stdin); 
    a[strcspn(a, "\n")] = 0;

    int length = strlen(a);
    int t = 0;

    for (int i = 0; i < length; i++) {
        if (a[i] != a[length - 1 - i]) {
            t = 1;
            break;
        }
    }

    if (t == 0)
        printf("Palindrome\n");
    else
        printf("Not a Palindrome\n");

    return 0;
}

