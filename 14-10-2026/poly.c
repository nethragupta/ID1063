#include<stdio.h>

typedef struct Polynomial
{
int n;
float a[21];
}poly;

int main(){
poly p,d;

int i;
float x,val=0,pw=1;

printf("enter degree: ");
scanf("%d",&p.n);
printf("enter coefficients a0 to a%d: ",p.n);
for(i=0;i<=p.n;i++)
scanf("%f",&p.a[i]);
printf("enter a: ");
scanf("%f", &x);
for(i=0;i<=p.n;i++){
val=val+p.a[i]*pw;
pw=pw*x;
}
printf("P(%.2f) = %.2f\n",x,val);

if(p.n==0){
d.n=0; d.a[0]=0;
}
else{
d.n=p.n-1;
for(i=1;i<=p.n;i++)
d.a[i-1]=i*p.a[i];
}

printf("derivative coefficients: ");
for(i=0;i<=d.n;i++)
printf("%.2f ",d.a[i]);
printf("\n");
return 0;
}

