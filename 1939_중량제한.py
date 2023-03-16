# 백준 1939
# 이진탐색 + BFS
from collections import deque
import sys

input = sys.stdin.readline

def bfs(mid):
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == end:
            return True
        for nx, nc in graph[now]:
            if visited[nx] == False and mid <= nc:
                q.append(nx)
                visited[nx] = True

    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

start, end = map(int, input().rstrip().split())
low, high = 1, 1000000000
while low <= high:
    visited = [False for _ in range(n + 1)]
    mid = (low + high) // 2
    if bfs(mid): # 목적지까지 도달이 가능하다면 low를 올림
        low = mid + 1
    else: # 목적지까지 불가능하다면 high를 내림
        high = mid - 1

print(high)