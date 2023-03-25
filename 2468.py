# 백준 2468
# 안전 영역
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
terrain = [list(map(int, input().rstrip().split()))for _ in range(n)]

def dfs(x, y, flood):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < n) and (0 <= ny < n) and not sunk[nx][ny] and terrain[nx][ny] > flood:
            sunk[nx][ny] = True
            dfs(nx, ny, flood)

ans = 1
for i in range(max(map(max, terrain))):
    sunk = [[False] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if terrain[j][k] > i and not sunk[j][k]:
                cnt += 1
                sunk[j][k] = True
                dfs(j, k, i)
    ans = max(ans, cnt)

print(ans)
    
    

