#!/usr/bin/python3
import mpmath
import sys
argv=sys.argv
mpmath.mp.dps = 200

def nthprime(n):
  s1=1
  for m in range(1,int(mpmath.power(2,n)+1)):
    s2=0
    for k in range(1,m+1):
      s2+=mpmath.floor(mpmath.power(mpmath.cos((mpmath.factorial(k-1)+1)/k*mpmath.pi),2))
    s1=s1+mpmath.floor(mpmath.power(n/s2,1/n))
  return(s1)

for i in range(1,100):
  print(int(nthprime(i)))
