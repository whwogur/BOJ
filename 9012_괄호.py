# 백준 9012

n = int(input())
for _ in range(n):
    stack = []
    a = input()
    isVPS = True

    for i in a:
        if i =='(':
            stack.append('(')
        if i == ')':
            if stack:
                stack.pop()
            elif not stack:
                isVPS = False
                break
    if not stack and isVPS:
        print('YES')
    elif stack or not isVPS:
        print('NO')
