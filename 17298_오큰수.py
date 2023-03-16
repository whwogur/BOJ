# 백준 #17298
# 스택
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
answer = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)