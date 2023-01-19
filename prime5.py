#!/usr/bin/python3
import sys

def primes(n):
  p = [i for i in range(n + 1)] # 0からｎまでの数のうち、
  for i in range(2, int(n**0.5)+1): # 2 から√ｎまでのうち、
   if p[i] != 0: # 最初の数が見つかったら
      for j in range(2, int(n/i)+1): # 倍数を次々と消してゆく
           p[i*j]=0
  return( [_ for _ in p if _ != 0][1:] ) # リストを整形する

argvs=sys.argv
n =int(argvs[1])
pl=primes(n)
print(pl)
print(len(pl))
