# 백준 2003
# 수들의 합 2
from sys import stdin
input = stdin.readline
n, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

_sum = nums[0]
left = 0
right = 1
cnt = 0

while True:
    if _sum < m:
        if right < n:
            _sum += nums[right]
            right += 1
        else:
            break
    elif _sum == m:
        cnt += 1
        _sum -= nums[left]
        left += 1
    else:
        _sum -= nums[left]
        left += 1

print(cnt)