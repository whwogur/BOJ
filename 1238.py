# 1238 파티
import sys
from heapq import*
input = sys.stdin.readline
INF = int(1e9)

n, m, party = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, dest):
    distance = [INF] * (n + 1)
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance[dest]

ansList = []
for i in range(1, n + 1):
    a = dijkstra(party, i) + dijkstra(i, party)
    ansList.append(a)

print(max(ansList)) 