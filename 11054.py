# 11054 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [0] + list(map(int, input().split()))
dp = [0 for _ in range(1001)]
ddp = [0 for _ in range(1001)]

for i in range(1, n + 1):
    dp[i] = 1
    for j in range(1, i + 1):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] += 1

for i in range(n, 0, -1):
    ddp[i] = 1
    for j in range(n, i-1, -1):
        if arr[i] > arr[j] and ddp[i] < ddp[j] + 1:
            ddp[i] += 1

ans = 0
for i in range(1, n + 1):
    if ans < dp[i] + ddp[i] - 1:
        ans = dp[i] + ddp[i] - 1

print(ans)