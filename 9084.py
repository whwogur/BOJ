# 9084 동전
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    units = list(map(int, input().split()))
    money = int(input().rstrip())

    dp = [0 for _ in range(money + 1)]
    dp[0] = 1

    for unit in units:
        for i in range(money + 1):
            if i >= unit:
                dp[i] += dp[i - unit]
    
    print(dp[money])