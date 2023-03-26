# 2253 점프
import sys
input = sys.stdin.readline

import sys
N, M = map(int, input().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
dp[1][0] = 0

small = set()
for _ in range(M):
    small.add(int(input().rstrip()))
for i in range(2, N + 1):
    if i in small:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))
