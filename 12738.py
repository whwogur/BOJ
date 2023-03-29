# 12738 가장 긴 증가하는 부분 수열3
from sys import stdin
import bisect
input = stdin.readline

n = int(input().rstrip())
nums = [0] + list(map(int, input().rstrip().split()))
dp = [0] * (n + 1)
cp = [-float('inf')]

for i in range(1, n+1):
    if nums[i] > cp[-1]:
        cp.append(nums[i])
        dp[i] = len(cp) - 1
    else:
        dp[i] = bisect.bisect_left(cp, nums[i])
        cp[dp[i]] = nums[i]

print(len(cp)-1)