# 17829 222풀링
import sys
input = sys.stdin.readline

n = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(n)]

def pooling(size, x, y):
    mid = size // 2
    if size == 2:
        answer = sorted([board[x][y], board[x+1][y],board[x][y+1], board[x+1][y+1]])
        return answer[-2]
    b2 = pooling(mid, x, y)
    b1 = pooling(mid, x+mid, y)
    b3 = pooling(mid, x, y+mid)
    b4 = pooling(mid, x+mid, y+mid)
    answer = sorted([b1, b2, b3, b4])
    return answer[-2]
print(pooling(n, 0, 0))