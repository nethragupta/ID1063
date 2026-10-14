#include <stdio.h>
#include <stdlib.h>

// one node = one term of the polynomial (coef * x^pow)
typedef struct node {
    float coef;          // coefficient of the term
    int pow;             // power of x
    struct node *next;   // pointer to the next term
} poly;

// creates a new term and attaches it at the end of the list
poly* add_term(poly *head, float c, int p) {
    poly *t = (poly*)malloc(sizeof(poly));
    t->coef = c;
    t->pow = p;
    t->next = NULL;

    // empty list: new node becomes the head
    if (head == NULL)
        return t;

    // otherwise walk to the last node and link the new one
    poly *q = head;
    while (q->next != NULL)
        q = q->next;
    q->next = t;
    return head;
}

int main() {
    poly *P = NULL;      // the polynomial
    poly *D = NULL;      // its derivative
    poly *q;             // used to walk through the lists
    int i = 0, ch;
    float c, x, val = 0, pw;

    // read coefficients a0 a1 a2 ... until Enter is pressed
    printf("enter coefficients a0 a1 a2 ... in one line: ");
    while (1) {
        scanf("%f", &c);
        P = add_term(P, c, i);   // i is the power of this term
        i++;

        // skip spaces after the number
        ch = getchar();
        while (ch == ' ' || ch == '\t')
            ch = getchar();

        // Enter means no more coefficients
        if (ch == '\n' || ch == EOF)
            break;

        // it was the start of the next number, put it back
        ungetc(ch, stdin);
    }

    printf("enter a: ");
    scanf("%f", &x);

    // (i) evaluate P(a): add coef * a^pow for every term
    for (q = P; q != NULL; q = q->next) {
        pw = 1;
        for (i = 0; i < q->pow; i++)
            pw = pw * x;
        val = val + q->coef * pw;
    }
    printf("P(%.2f) = %.2f\n", x, val);

    // (ii) derivative: c*x^p becomes (c*p)*x^(p-1)
    // constant term (p = 0) disappears, so skip it
    for (q = P; q != NULL; q = q->next) {
        if (q->pow != 0)
            D = add_term(D, q->coef * q->pow, q->pow - 1);
    }

    // print the derivative
    printf("P'(x) = ");
    if (D == NULL)
        printf("0");     // derivative of a constant
    for (q = D; q != NULL; q = q->next) {
        printf("%.2fx^%d", q->coef, q->pow);
        if (q->next != NULL)
            printf(" + ");
    }
    printf("\n");

    // free all the nodes
    while (P != NULL) {
        q = P;
        P = P->next;
        free(q);
    }
    while (D != NULL) {
        q = D;
        D = D->next;
        free(q);
    }

    return 0;
}

