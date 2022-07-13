import sys

N, K = map(int, sys.stdin.readline().split())
x, cnt = 1,0
while x * K <= N:
    x *= K
    cnt += 1
print(cnt + N - x)