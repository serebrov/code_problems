# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

from collections import Counter
from math import factorial

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r) )

def process(w):
    result = 0
    counts = Counter()
    result = 0
    length = len(w)
    for ll in range(1,length):
        for i in range(0,length-ll+1):
            h = list(w[i:i+ll])
            h.sort()
            counts[str(h)] += 1
    for hsh in counts:
        value = counts[hsh]
        if value > 1:
            result += value * (value-1) / 2
    return int(result)


T = int(input().strip())
for t in range(T):
    w = input().strip()
    print(process(w))
