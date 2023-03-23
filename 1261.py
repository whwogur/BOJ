# 1261 알고스팟
import sys
from heapq import*
input = sys.stdin.readline

m, n = map(int, input().split())
board = [[0] * (m + 1)]
board += [[0] + list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * (m + 1) for _ in range(n + 1)]

def dijkstra():
    dx = (1, -1, 0, 0)
    dy = (0, 0, -1, 1)
    heap = []
    heappush(heap, [0, 1, 1])
    visited[1][1] = 1

    while heap:
        a, x, y = heappop(heap)
        if x == n and y == m:
            print(a)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if n >= nx > 0 < ny <= m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if not board[nx][ny]:
                    heappush(heap, [a, nx, ny])
                else:
                    heappush(heap, [a+1, nx,ny])

dijkstra()