# 12865 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stuff = [(0, 0)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    stuff.append(tuple(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    
print(dp[n][k])