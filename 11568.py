# 11568 민균이의 계략
import sys
input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().split()))
dp = [numbers[0]]
def lowerBound(list, num):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        if num <= list[mid]:
            high = mid
        elif num > list[mid]:
            low = mid + 1
    return high

for i in range(1,n):
    if dp[-1] < numbers[i]:
        dp.append(numbers[i])
    else:
        dp[lowerBound(dp,numbers[i])] = numbers[i]

print(len(dp))
