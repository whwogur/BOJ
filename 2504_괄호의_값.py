# 백준 2504
# 괄호의 값
import sys
input = sys.stdin.readline

# 짝이 안맞으면 0
bracket = list(input().rstrip())
length = len(bracket)
stack = []
answer = 0
tmp = 1

for i in range(length):
    if bracket[i] == '(':
        stack.append(bracket[i])
        tmp *= 2
    
    elif bracket[i] == '[':
        tmp *= 3
        stack.append(bracket[i])
    
    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if bracket[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break

        if bracket[i-1] == '[':
            answer += tmp
        
        stack.pop()
        tmp //= 3

if stack:
    answer = 0
print(answer)