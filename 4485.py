# 4485 녹색 옷 입은 애 젤다지?
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    rupee[0][0] = 0

    while q:
        currRupee, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {T}: {rupee[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if n > nx >= 0 <= ny < n:
                nextRupee = currRupee + graph[nx][ny]

                if nextRupee < rupee[nx][ny]:
                    rupee[nx][ny] = nextRupee
                    heapq.heappush(q, (nextRupee, nx, ny))

T = 1

while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    rupee = [[INF] * n for _ in range(n)]

    dijkstra()
    T += 1