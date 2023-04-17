# 10610 30
import sys
input = sys.stdin.readline

nums = list(input().rstrip())
nums.sort(reverse=True)
sum = 0
if '0' not in nums:
    print(-1)
else:
    for num in nums:
        sum += int(num)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(nums))