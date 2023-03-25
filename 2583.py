# 2583 영역 구하기
import sys
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if m > ny >= 0 <= nx < n and board[ny][nx] == 0:
                board[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
    return cnt

m, n, k = map(int, input().split())
board = [[0]* n for _ in range(m)]
visited = [[False] * m for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
for _ in range(k):
    a, b, c, d = map(int,input().split())
    for i in range(b, d):
        for j in range(a, c):
            board[i][j] = 1

areas = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = 1
            areas.append(bfs(i, j))

print(len(areas))
print(*sorted(areas))

    
