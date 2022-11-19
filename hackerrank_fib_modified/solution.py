# https://www.hackerrank.com/challenges/fibonacci-modified/problem

# 0 1 5
t1, t2, n = input().strip().split(' ')
t1, t2, n = int(t1), int(t2), int(n)

for i in range(2, n):
    tn = t1 + t2*t2
    t1 = t2
    t2 = tn
print(tn)
