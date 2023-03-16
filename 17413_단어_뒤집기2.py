# 백준 17413

import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
tag = False
result = ''

for i in s:
    if i == ' ':
        while stack:
            result += stack.pop()
        result += i
    
    elif i == '<':
        while stack:
            result += stack.pop()
        tag = True
        result += i

    elif i == '>':
        tag = False
        result += i

    elif tag:
        result += i

    else:
        stack.append(i)

while stack:
    result += stack.pop()

print(result)
