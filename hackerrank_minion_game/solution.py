# https://www.hackerrank.com/challenges/the-minion-game/problem

S = input()
length = len(S)
kevin = 0 
stuart = 0 
for i in range(0,length):
    num = length-i
    if S[i] in ['A','E','I','O','U']:
        kevin += num
    else:
        stuart += num

if kevin == stuart:
    print('Draw')
elif kevin > stuart:
    print('Kevin',kevin)
else:
    print('Stuart',stuart)
