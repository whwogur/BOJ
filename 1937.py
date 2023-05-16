# 욕심쟁이 판다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)

def dfs(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if n > nx >= 0 <= ny < n and board[nx][ny] > board[x][y]:
                dp[x][y] = max(dp[x][y],dfs(nx,ny))
    
    return dp[x][y]+1

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
            
print(ans)