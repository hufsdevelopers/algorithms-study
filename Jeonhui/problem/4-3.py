import sys


def move(x, y, d):
    global N, M, Map
    if not (0 <= y < N and 0 <= x < M) or Map[y][x] == 1:
        return 0
    Map[y][x] = 1
    m = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    a = move(x + m[d][0], y + m[d][1], d)
    b = move(x + m[(d + 1) % 4][0], y + m[(d + 1) % 4][1], (d + 1) % 4)
    c = move(x + m[(d + 2) % 4][0], y + m[(d + 2) % 4][1], (d + 2) % 4)
    d = move(x + m[(d + 3) % 4][0], y + m[(d + 3) % 4][1], (d + 3) % 4)
    return a + b + c + d +  1


N, M = map(int, sys.stdin.readline().split())
posX, posY, d = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(move(posX, posY, d))
