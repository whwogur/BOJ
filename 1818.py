# 1818 책정리
import sys
input = sys.stdin.readline

def lowerbound(list, num):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (high + low) // 2
        if list[mid] < num:
            low = mid + 1
        elif list[mid] >= num:
            high = mid
    return high

n = int(input().rstrip())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        dp[lowerbound(dp, arr[i])] = arr[i]
print(n - len(dp))