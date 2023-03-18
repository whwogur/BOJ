# 백준 2573 빙산(DFS풀이)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(i, j):
    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
            visited[nx][ny] = False
            if glacier[nx][ny] != 0:
                dfs(nx, ny)

n, m = map(int, input().rstrip().split())
glacier = [list(map(int, input().rstrip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
years = 0

while True:
    years += 1
    for i in range(n):
        for j in range(m):
            if glacier[i][j] != 0:
                visited[i][j] = True
                tmp = glacier[i][j]
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        if glacier[nx][ny] == 0:
                            tmp -= 1
                            if tmp == 0:
                                break
                glacier[i][j] = tmp
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if glacier[i][j] != 0 and visited[i][j]:
                dfs(i, j)
                cnt += 1
            elif glacier[i][j] == 0 and visited[i][j]:
                visited[i][j] = False

    if cnt >= 2: # 영역이 2개 이상
        print(years)
        break
    elif cnt == 0: # 한번에 다 녹았다
        print(0)
        break