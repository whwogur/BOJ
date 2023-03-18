# 2665 미로 만들기
import sys
from heapq import*
input = sys.stdin.readline

n = int(input().rstrip())
board = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dijkstra():
    dx = (1, -1, 0, 0)
    dy = (0, 0, -1, 1)
    heap = []
    heappush(heap, [0, 0, 0])
    visited[0][0] = 1

    while heap:
        a, x, y = heappop(heap)
        if x == n - 1 and y == n - 1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n > nx >= 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                if not board[nx][ny]:
                    heappush(heap, [a + 1, nx, ny])
                else:
                    heappush(heap, [a, nx, ny])

dijkstra()