import sys

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
st = sys.stdin.readline()
pos = [ord(st[0]) - ord('a') + 1, int(st[1])]
print(len([0 for step in steps if 0 < pos[0] + step[0] <= 8 and 0 < pos[1] + step[1] <= 8]))
