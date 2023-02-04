#include  <stdio.h>
#include  <stdlib.h>

int primes(int n) {
    char f[n];
    int c=1;
    printf("2 ");
    for (int j=0;j<=n;j++) f[j]=1;
    for (int j=0;j<=n;j++)
       if (f[j]) {
           int p=j*2+3;
           printf("%d ",p);
           for (int k=j+p;k<=n;k+=p) f[k]=0;
           c++;
           }
    return(c);
}

int main(int argc,char *argv[]) {
    int m=atoi(argv[1]),c;
    c = primes((m-3)/2);
    printf("\n%d Primes\n",c);
}
