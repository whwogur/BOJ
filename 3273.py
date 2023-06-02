import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

cnt = 0
i, j = 0, n-1
nums.sort()
while i < j:
    temp = nums[i] + nums[j]
    if temp == x:
        cnt += 1
        i += 1
        j -= 1
    elif temp < x:
        i += 1
    else:
        j -= 1

print(cnt)