# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import sys

#n = int(input().strip())
#c = map(int,input().strip().split(' '))

# 6
# 0 0 0 0 1 0

N = int(input().strip())
t = list(map(lambda x: int(x), input().strip().split(' ')))

E = [float('Inf') for i in range(N)]
E[0] = 0

for i in range(1, N):
    if t[i-1] == 1:
        E[i] = E[i-2] + 1
    elif t[i-2] == 1:
        E[i] = E[i-1] + 1
    else:
        E[i] = min(E[i-1], E[i-2]) + 1
#print E
print(E[N-1])
