# 2178 미로 탐색

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y,start_x))

    while q:
        _y, _x = q.popleft()
        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]

            if y > ny >= 0 <= nx < x and board[ny][nx] == 1:
                board[ny][nx] = board[_y][_x] + 1
                q.append((ny, nx))
    return board[y - 1][x - 1]

y, x = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(y)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs(0, 0))