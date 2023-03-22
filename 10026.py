# 10026 적록색약
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input().rstrip())
board = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False]* n for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
count = 0
cb_count = 0
def colorBlind(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if n > nx >= 0 <= ny < n and not visited[nx][ny]:
            if board[nx][ny] == board[x][y]:
                colorBlind(nx,ny)

for color in ['R','G','B']:
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == color:
                colorBlind(i, j)
                count += 1

visited = [[False]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for color in ['R','B']:
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == color:
                colorBlind(i, j)
                cb_count += 1

print(count, cb_count)
