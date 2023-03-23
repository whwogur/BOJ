# 1904 01타일
import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [[]for _ in range(n + 1)]

dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])