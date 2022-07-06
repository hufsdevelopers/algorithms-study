import sys

n, M, K = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())), key=lambda x: -x)
print(A[0] * (M if K > M else K) + A[1] * (0 if K > M else (M - K)))
print(A[0] * (M if K > M else K), A[1] * (0 if K > M else (M - K)))