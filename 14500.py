# 14500 테트로미노
import sys
input = sys.stdin.readline

def dfs(x, y, depth, cnt):
    global ans
    if ans >= cnt + max_val * (4 - depth):
        return
    if depth == 4:
        ans = max(ans, cnt)
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if n > nx >= 0 <= ny < m and not visited[nx][ny]:
                if depth == 2:
                    visited[nx][ny] = True
                    dfs(x, y, depth + 1, cnt + board[nx][ny])
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, cnt + board[nx][ny])
                visited[nx][ny] = False

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = -1e9
max_val = max(map(max, board))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)