import sys


def ice(x, y):
    global iceMold
    if 0 > x or x >= M or 0 > y or y >= N:
        return False
    if iceMold[y][x] == 1:
        return False
    iceMold[y][x] = 1
    ice(x - 1, y)
    ice(x + 1, y)
    ice(x, y - 1)
    ice(x, y + 1)
    return True


N, M = map(int, sys.stdin.readline().split())
iceMold = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]
res = 0
for y in range(N):
    for x in range(M):
        if iceMold[y][x] == 0:
            if ice(x, y):
                res += 1
print(res)
