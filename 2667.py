import sys
input = sys.stdin.readline
from collections import deque
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    while q:
        _x, _y = q.popleft()
        for i in range(4):
            nx, ny = _x + dx[i], _y + dy[i]
            if n > nx >= 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
                board[nx][ny] = board[_x][_y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    if cnt == 1:
        compounds.append(cnt)
    else:
        compounds.append(cnt - 1)

                
n = int(input().rstrip())
board = [list(map(int, input().rstrip())) for _ in range(n)]
compounds = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(len(compounds))
print(*sorted(compounds), sep='\n')