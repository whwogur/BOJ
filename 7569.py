# 7569 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
q = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i,j,k])
    graph.append(tmp)

dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, 1, -1, 0, 0)
dz = (0, 0, 0, 0, 1, -1)

while q:
    x, y, z = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if h > nx >= 0 <= ny < n and 0 <= nz < m and not graph[nx][ny][nz]:
            q.append([nx,ny,nz])
            graph[nx][ny][nz] = graph[x][y][z] + 1

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day - 1)