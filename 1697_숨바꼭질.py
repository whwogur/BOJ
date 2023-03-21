# 1697 숨바꼭질

import sys
from collections import deque

def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            print(dist[now])
            break
        for nx in (now - 1, now + 1, now * 2):
            if 0 <= nx <= MAX and dist[nx] == 0:
                dist[nx] = dist[now] + 1
                q.append(nx)

MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()