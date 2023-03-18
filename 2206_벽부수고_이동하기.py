# 2206 벽부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(2)]
q = deque()
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

def bfs():
    q.append((0, 0, 0))  # x, y, c(chance)
    visited[0][0][0] = 1  # c, x, y
    while q:
        x, y, c = q.popleft()
        if x == n-1 and y == m-1:
            return visited[c][x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if n > nx >= 0 <= ny < m:
                if not visited[c][nx][ny]:
                    if not board[nx][ny]:
                        visited[c][nx][ny] = visited[c][x][y] + 1
                        q.append((nx, ny, c))
                    elif board[nx][ny] and not c:
                        visited[1][nx][ny] = visited[c][x][y] + 1
                        q.append((nx, ny, 1))
    return -1

print(bfs())

