# 4-1) 상하좌우
import sys

d = {'R': (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
pos = [1, 1]
n = int(sys.stdin.readline())
move = [d[r] for r in sys.stdin.readline().split()]
for x, y in move:
    if 0 < pos[0] + x < n:
        pos[0] += x
    if 0 < pos[1] + y < n:
        pos[1] += y
print(pos[0], pos[1])
