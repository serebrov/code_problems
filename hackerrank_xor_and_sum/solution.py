# https://www.hackerrank.com/challenges/xor-and-sum/problem

# Note: this is not an proper solution, just a test of a
# straighforward approach, it works with python.
# A proper solution would avoid the direct calculation as
# we are working with large numbers here, the task is
# in the dynamic programming section which hints that
# solution could be based on dynamic programming.

a_str = input().strip()
a = int(a_str, base=2)
b_str = input().strip()
b = int(b_str, base=2)

mod = 10**9+7
result = 0
for i in range(0, 314159+1):
    result += (a ^ (b << i))
    #result += nand(a, b << i) % mod
    #result += (a ^ (b << i)) % mod
    #result += (~(a & (b << i))) % mod
    #result += (a ^ (b * my2power(i))) % mod
print (result % mod)
