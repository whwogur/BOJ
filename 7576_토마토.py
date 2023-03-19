# 7576 토마토

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))
cnt = 0
while q:
    cnt += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if n > nx >= 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
print(cnt - 1)
