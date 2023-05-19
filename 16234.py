from collections import deque
import sys
input = sys.stdin.readline
dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)
def bfs(i, j):
    q = deque()
    q.append([i, j])
    allies = []
    allies.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(countries[nx][ny] - countries[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    allies.append([nx, ny])
    return allies

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
while True:
    visit = [[0] * n for i in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                allies = bfs(i, j)
                if len(allies) > 1:
                    flag = True
                    num = sum([countries[x][y] for x, y in allies]) // len(allies)
                    for x, y in allies:
                        countries[x][y] = num
    if not flag:
        break
    cnt += 1
print(cnt)
