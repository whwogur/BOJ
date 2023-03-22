# 7562 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline

dx = (-2, -1, 1, 2, 2, 1, -1, -2)
dy = (1, 2, 2, 1, -1, -2, -2, -1)
def bfs(x, y, num):
    q = deque()
    q.append([x, y])
    board[x][y] = num
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if l > nx >= 0 <= ny < l and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])
            if nx == dest_x and ny == dest_y:
                return board[nx][ny]
                

T = int(input().rstrip())
for _ in range(T):
    l = int(input().rstrip())
    knight_x, knight_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    board = [[-1] * l for _ in range(l)]

    print(bfs(knight_x, knight_y, 0))
    
    
