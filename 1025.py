import sys
input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]
answer = -1

def sqr(num):
    S = int(num)
    return int(num ** 0.5) ** 2 == num

for i in range(N):
    for j in range(M):
        for row_d in range(-N,N): # 행의 등차
            for col_d in range(-M,M): # 열의 등차
                num = ""
                x,y = i,j
                if row_d == 0 and col_d == 0:
                    continue
                while 0 <= x < N and 0 <= y < M:
                    num += board[x][y]
                    if sqr(num):
                        answer = max(answer,int(num))
                    x += row_d
                    y += col_d
print(answer)