# 4179 불!
import sys
from collections import deque
INF = int(1e9)
input = sys.stdin.readline


def bfs(queue, visited):

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if r > nx >= 0 <= ny < c:
                if visited[nx][ny] == 0 and board[nx][ny] != '#':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited


r, c = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(r)]

answer = INF
fire_q, jihon_q = deque(), deque()
fire_visited, jihon_visited = [[0] * c for _ in range(r)], [[0] * c for _ in range(r)]

for x in range(r):
    for y in range(c):
        if board[x][y] == 'J':
            jihon_q.append((x, y))
            jihon_visited[x][y] = 1
        elif board[x][y] == 'F':
            fire_q.append((x, y))
            fire_visited[x][y] = 1

jihon_visited = bfs(jihon_q, jihon_visited)
fire_visited = bfs(fire_q, fire_visited)

for x in range(r):
    for y in range(c):
        if jihon_visited[x][y] > 0:
            if jihon_visited[x][y] < fire_visited[x][y] or fire_visited[x][y] == 0:
                if x == 0 or y == 0 or x == (r-1) or y == (c-1):
                    answer = min(answer, jihon_visited[x][y])

print(answer if answer != INF  else "IMPOSSIBLE")
