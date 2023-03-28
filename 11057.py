# 11057 오르막 수
import sys
input = sys.stdin.readline

n = int(input().rstrip())
answer = 0
dp = [[0]*10 for _ in range(1001)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][0] = 1
            continue
        dp[i][j] = (dp[i - 1][j] + dp[i][j-1]) % 10007

for i in range(10):
    answer += dp[n][i]
print(answer % 10007)