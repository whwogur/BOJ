# 2579 계단 오르기
import sys
input = sys.stdin.readline
MAX = 301
n = int(input().rstrip())
dp = [0] * MAX
stairs = [0] * MAX
for i in range(1, n + 1):
    stairs[i] = int(input().rstrip())
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
if n < 3:
    print(dp[n])
    exit(0)
else:
    for i in range(3, MAX):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
    print(dp[n])