import sys

N,M = map(int, sys.stdin.readline().split())
print(max([min(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]))