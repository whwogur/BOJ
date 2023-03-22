# 1389 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])

    while q:
        x  = q.popleft()
        for e in adj[x]:
            if not visited[e]:
                visited[e] = visited[x] + 1
                q.append(e)
            

n, e = map(int, input().split())
adj = [[]for _ in range(n + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

answer = []

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    answer.append(sum(visited))

print(answer.index(min(answer)) + 1)