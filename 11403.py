# 11403 경로 찾기
import sys
input = sys.stdin.readline
n = int(input().rstrip())
matrix = [list(map(int, input().split())) for _ in range(n)]

def dfs(x):
    for i in range(n):
        if matrix[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()