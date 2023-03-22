# 1987 알파벳
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
alpha = set()
count = 0
def dfs(x, y, cnt):
    global count
    count = max(count, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if n > nx >= 0 <= ny < m and board[nx][ny] not in alpha:
            alpha.add(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            alpha.remove(board[nx][ny])

alpha.add(board[0][0])
dfs(0, 0, 1)
print(count)