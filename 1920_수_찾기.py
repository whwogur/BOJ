# 백준 1920
# 수 찾기

import sys
input = sys.stdin.readline
# 방법 1 - 집합으로 만들어 탐색

# N = int(input().rstrip())
# A = set(map(int, input().rstrip().split()))
# M = int(input().rstrip())
# nums = list(map(int, input().rstrip().split()))

# for i in range(M):
#     print(1) if nums[i] in A else print(0)

# 방법 2 - 이분탐색

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
arr.sort()
for num in nums:
    start, end = 0, n-1
    found = False

    # 이분탐색
    while start <= end:
        mid = (start + end) // 2
        if num == arr[mid]:
            found = True
            print(1)
            break
        elif num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if not found:
        print(0)