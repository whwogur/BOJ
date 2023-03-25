# 백준 17299
# 스택
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)

    