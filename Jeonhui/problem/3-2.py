import sys

n, M, K = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())), key=lambda x: -x)
sum, x = 0, 0
for i in range(M):
    sum += A[0] if i%K != K-1 else A[1]
print(sum)
