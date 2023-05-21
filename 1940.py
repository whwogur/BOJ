# 1940 주몽
import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0
left, right = 0, n - 1
while left < right:
    if nums[left] + nums[right] == m:
        cnt += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] < m:
        left += 1
    else:
        right -= 1

print(cnt)