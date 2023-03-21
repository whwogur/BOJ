# 13548 숨바꼭질3
from collections import deque
MAX = 100000
visited = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)

n, k = map(int, input().split())
q = deque()
q.append(n)
visited[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now * 2 <= MAX and visited[now * 2] == False:
        q.appendleft(now * 2)
        visited[now * 2] = True
        dist[now * 2] = dist[now]
    if now + 1 <= MAX and visited[now + 1] == False:
        q.append(now + 1)
        visited[now + 1] = True
        dist[now + 1] = dist[now] + 1
    if now - 1 >= 0 and visited[now - 1] == False:
        q.append(now - 1)
        visited[now - 1] = True
        dist[now - 1] = dist[now] + 1

print(dist[k])