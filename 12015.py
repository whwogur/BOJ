# 12015 가장 긴 증가하는 부분 수열 2
from sys import stdin
input = stdin.readline

n = int(input())
sequences = list(map(int, input().rstrip().split()))
inc_ss = [0]

for i in sequences:
    if inc_ss[-1] < i:
        inc_ss.append(i)
    else:
        left = 0
        right = len(inc_ss)

        while left < right:
            mid = (right + left) // 2
            if inc_ss[mid] < i:
                left = mid + 1
            else:
                right = mid
        inc_ss[right] = i

print(len(inc_ss) - 1)

# from bisect import bisect_left

# n = int(input())
# array = list(map(int, input().split()))
# stack = [0]

# for i in array:
#     if stack[-1] < i:
#         stack.append(i)
#     else:
#         stack[bisect_left(stack, i)] = i

# print(len(stack)-1)