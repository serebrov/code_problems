# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

K, M = map(int, input().split())
data = []
for i in range(K):
    data.append(list(map(int, input().split()))[1:])
S = 0
for line in product(*data):
    result = 0
    for n in line:
        result += n**2
    S = max(S, result % M)
print(S%M)
