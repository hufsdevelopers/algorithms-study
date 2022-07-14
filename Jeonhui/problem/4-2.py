import sys

n = int(sys.stdin.readline())
cnt = 0
for H in range(n + 1):
    for M in range(60):
        for S in range(60):
            if '3' in f"{H}{M}{S}":
                cnt += 1
print(cnt)
