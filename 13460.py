# 13460 구슬탈출 2
import sys
from collections import deque
input = sys.stdin.readline

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    cnt = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if cnt > 10:
                print(-1)
                return
            if board[rx][ry] == 'O':
                print(cnt)
                return
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if board[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if board[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if board[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if board[nbx][nby] == 'O':
                        break
                if board[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
    print(-1)


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(str, input())))
    for j in range(m):
        if board[i][j] == 'B':
            bx, by = i, j
        elif board[i][j] == 'R':
            rx, ry = i, j
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

bfs(rx, ry, bx, by)
