# 백준 2470
# 두 용액
# 투 포인터 문제

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
arr.sort()

left = 0
right = n-1

diff = abs(arr[left] + arr[right])
answer = [arr[left], arr[right]]

while left < right:
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val

    if abs(sum) < diff:
        diff = abs(sum)
        answer = [left_val, right_val]
        if diff == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])

