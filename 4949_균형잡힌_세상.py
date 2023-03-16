# 백준 4949
# 스택
import sys
input = sys.stdin.readline

stack = []

while True:
    string = input().rstrip()
    if string == '.':
        break
    stack = []
    balanced = True
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                balanced = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                balanced = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if balanced == True and not stack:
        print('yes')
    else:
        print('no')