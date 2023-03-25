# 18352 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split()) # [x:출발도시]
adj = [[] for _ in range(n + 1)] # [n:도시개수] [m:간선개수] [k:거리]
visited = [False] * (n + 1)
qual = []
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b)

def bfs(start):
    distance = 0
    q = deque()
    visited[start] = True
    q.append((start,distance))
    while q:
        vertex, dist = q.popleft()
        if dist == k:
            qual.append(vertex)
        for i in adj[vertex]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist + 1))

bfs(x)
qual.sort()
if qual:
    print(*qual, sep='\n')
else:
    print(-1)