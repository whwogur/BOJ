# 1932 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            left = 0
        else:
            left = dp[i - 1][j - 1]
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(up, left)
print(max(dp[n - 1]))