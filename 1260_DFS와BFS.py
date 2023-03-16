# 백준 1260
import sys
from collections import deque
input = sys.stdin.readline

def dfs(adjacent, check_2, a):
    check_2[a] = True
    print(a, end=' ')

    for i in adjacent[a]:
        if not check[i]:
            dfs(adjacent, check_2, i)

def bfs(adjacent, check, start):
    q = deque([start])
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')

        for i in adjacent[x]:
            if not check[i]:
                q.append(i)
                check[i] = True

n, m, v = map(int, input().rstrip().split())

adjacent = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

for i in adjacent:
    i.sort()

check = [False] * (n + 1)
dfs(adjacent, check, v)
check = [False] * (n + 1)
print()
bfs(adjacent, check, v)


