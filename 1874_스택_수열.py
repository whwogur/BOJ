# 백준 1874
from sys import stdin
input = stdin.readline

n = int(input().rstrip())
stack = []
ans = []
found = True

now = 1
for _ in range(n):
    num = int(input().rstrip())
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        found = False

if not found:
    print('NO')
else:
    print(*ans,sep='\n')