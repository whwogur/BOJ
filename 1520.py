# 1520 내리막 길
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
memo = [[-1] * m for _ in range(n)]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if memo[x][y] != -1:
        return memo[x][y]
    
    routes = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if n > nx >= 0 <= ny < m and board[x][y] > board[nx][ny]:
            routes += dfs(nx, ny)

    memo[x][y] = routes
    return memo[x][y]

print(dfs(0, 0))