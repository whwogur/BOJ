# 10942 팰린드롬?
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n - 1):
    if arr[i] == arr[i + 1]: dp[i][i+1] = 1

for i in range(2, n):
    for j in range(n - i):
        if arr[j] == arr[i + j] and dp[j + 1][i + j - 1] == 1:
            dp[j][i + j] = 1

for i in range(int(input().rstrip())):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])
