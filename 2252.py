# 백준 2252
# 줄세우기
from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().rstrip().split())
degree = [[] for _ in range(n+1)]
num = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().rstrip().split())
    degree[a].append(b)
    num[b] += 1

q = deque()
for i in range(1, n+1):
    if num[i] == 0:
        q.append(i)

result = []
while q:
    cu = q.popleft()
    result.append(cu)
    for i in degree[cu]:
        num[i] -= 1
        if num[i] == 0:
            q.append(i)

print(*result)