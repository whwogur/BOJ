# 12014 주식
import sys
input = sys.stdin.readline
def lowerBound(list, num):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        if list[mid] < num:
            low = mid + 1
        elif list[mid] >= num:
            high = mid
    return high

T = int(input().rstrip())
for t in range(1,T+1):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    dp = [prices[0]]
    
    for i in range(1, n):
        if dp[-1] < prices[i]:
            dp.append(prices[i])
        else:
            dp[lowerBound(dp, prices[i])] = prices[i]
    if len(dp) >= k:
        print("Case #%d" %(t))
        print(1)
    else:
        print("Case #%d" %(t))
        print(0)