# 3085 사탕게임
import sys
input = sys.stdin.readline

n = int(input().rstrip())
board = [list(map(str, input().rstrip())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def check():
    global answer
    r_score, c_score, r_max, c_max = 1, 1, -1e10, -1e10
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] == board[i][j+1]:
                r_score += 1
            else:
                r_score = 1
            r_max = max(r_score, r_max)
        r_score = 1
    for i in range(n):
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                c_score += 1
            else:
                c_score = 1
            c_max = max(c_score, c_max)
        c_score = 1
    answer = max(answer,r_max,c_max)

answer = -1e9
for x in range(n):
    for y in range(n):
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if n > nx >= 0 <= ny < n and board[nx][ny] != board[x][y]:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                check()
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
print(answer)