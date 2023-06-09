# 17070 파이프 옮기기1
import sys
input = sys.stdin.readline

def dfs(pos):
    global cnt
    x, y, z = pos

    if x == n - 1 and y == n - 1:
        cnt += 1
        return
    
    if x + 1 < n and y + 1 < n:
        if board[x + 1][y + 1] != 1 and board[x][y + 1] != 1 and board[x + 1][y] != 1:
            dfs((x + 1, y + 1, 2))
    
    if z == 0 or z == 2:
        if y + 1 < n:
            if board[x][y + 1] != 1:
                dfs((x, y + 1, 0))
    
    if z == 1 or z == 2:
        if x + 1 < n:
            if board[x + 1][y] != 1:
                dfs((x + 1, y, 1))

n = int(input().rstrip())
board = [list(map(int, input().split()))for _ in range(n)]
cnt = 0    

dfs((0, 1, 0))
print(cnt)