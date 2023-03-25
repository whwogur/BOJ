# 백준 6549
# 스택
from sys import stdin
input = stdin.readline

rectangles = []

while True:
    a = list(map(int, input().rstrip().split()))
    if a[0] == 0:
        break
    ans = 0
    stack = []
    rectangles = a[1:]

    for rectangle in rectangles:
        tmp = 0
        while stack and stack[-1][0] > rectangle:
            tmp += stack[-1][1]
            ans = max(ans, tmp * stack[-1][0])
            stack.pop()
        
        tmp += 1
        stack.append([rectangle, tmp])

    tmp = 0
    while stack:
        tmp += stack[-1][1]
        ans = max(ans, tmp * stack[-1][0])
        stack.pop()
    
    print(ans)