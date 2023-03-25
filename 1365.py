# 1365 꼬인 전깃줄
import sys
input = sys.stdin.readline

def binarySearch(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if sequence[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

n = int(input().rstrip())
numbers = list(map(int, input().split()))
sequence = [numbers[0],]

for i in range(1, n):
    if sequence[-1] < numbers[i]:
        sequence.append(numbers[i])
    else:
        idx = binarySearch(0, len(sequence)-1, numbers[i])
        sequence[idx] = numbers[i]
        
print(n - len(sequence))