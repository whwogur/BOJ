# 1504 특정한최단경로
import sys
from heapq import*
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
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
    
    return distance

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int,input().split())

original_list = dijkstra(1)
v1_list = dijkstra(v1)
v2_list = dijkstra(v2)

v1_path = original_list[v1] + v1_list[v2] + v2_list[n]
v2_path = original_list[v2] + v2_list[v1] + v1_list[n]

answer = min(v1_path, v2_path)
print(answer if answer < INF else -1)