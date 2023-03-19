# 3055 탈출
from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

hedge_x, hedge_y = 0, 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == "S":
            hedge_x, hedge_y = i, j
            graph[i][j] = "."

def flood():
    water = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "*" and not visited[i][j]:
                water.append((i, j))
                visited[i][j] = True

    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if R > nx >= 0 <= ny < C and not visited[nx][ny]:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0

    while q:
        cnt += 1
        flood()

        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if R > nx >= 0 <= ny < C and not visited[nx][ny]:
                    if graph[nx][ny] == '.':
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    elif graph[nx][ny] == 'D':
                        return cnt
    return "KAKTUS"

print(bfs(hedge_x, hedge_y))