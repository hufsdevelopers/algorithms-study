import sys
coin = [500,100,50,10]
n = int(sys.stdin.readline())
cnt = 0
for c in coin:
    cnt += n//c
    n %= c
print(cnt)