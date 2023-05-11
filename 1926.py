# 1926 그림
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)
q = deque()

pict_cnt, maxpict = 0, -1e9
for i in range(n):
    for j in range(m):
        pict = 0
        if not visited[i][j]:
            if paper[i][j]:
                q.append((i, j))
                visited[i][j] = True
                pict_cnt += 1
                pict += 1
            
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if n > nx >= 0 <= ny < m and paper[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        pict += 1
                        q.append((nx, ny))
            maxpict = max(pict, maxpict)
print(pict_cnt)
print(maxpict)