# 2352 반도체 설계
import sys
from bisect import bisect
input = sys.stdin.readline

n = int(input().rstrip())
sequence = list(map(int, input().split()))
dp = [sequence[0]]

for i in range(1, n):
    if dp[-1] < sequence[i]:
        dp.append(sequence[i])
    else:
        dp[bisect(dp, sequence[i])] = sequence[i]

print(len(dp))