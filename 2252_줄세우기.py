# 2252 줄세우기
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

answer = []
while q:
    tmp = q.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

print(*answer)