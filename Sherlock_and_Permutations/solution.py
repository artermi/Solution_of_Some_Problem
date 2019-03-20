#!/bin/python3

import os
import sys

# Complete the solve function below.

def fast_pow (Num,Pow,Mod):
    ans = 1
    base = Num
    while Pow > 0:
        if Pow % 2 == 1:
            Pow = Pow -1
            ans = (ans * base) % Mod
        Pow = Pow / 2
        base = (base * base) % Mod

    return int(ans % Mod)

        

def solve(n, m):
    #compute factorial of C(m+n-1,n) % prime
    upper = 1
    lower_m = 1 
    Chigh = m+n-1
    Clow = min(n,m-1)
    Prime = 1000000000 + 7
    #Calculate (u%p)*(l^(p-2) % p)%p
    for i in range(Clow):
        upper = ( upper * (Chigh-i) ) % Prime
        lower_m = (lower_m * fast_pow(Clow-i,Prime-2,Prime) ) % Prime

    return int((upper * lower_m) % Prime)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

