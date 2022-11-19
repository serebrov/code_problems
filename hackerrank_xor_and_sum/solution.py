# https://www.hackerrank.com/challenges/xor-and-sum/problem

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
