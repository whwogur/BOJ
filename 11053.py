# 11053 가장 긴 증가하는 부분수열
import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [1] * n
arr = list(map(int, input().split()))

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))