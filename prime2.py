#!/usr/bin/python3
#
#試し割り法による素数の生成
#
def trial_division(t):
  for i in range(2,t):
    if t % i == 0:
      return(0)
  return(1)
 
def nth_prime(n):
  m=2
  primes=[]
  while(1):
    if (trial_division(m)==1):
      primes.append(m)
      if (len(primes)==n):
        return(primes[n-1])
    m=m+1

n=1
while(1):
  print(nth_prime(n))
  n=n+1
