# 14938 서강그라운드
import sys
from heapq import*
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    dist = [INF] * (n + 1)
    heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, now = heappop(q)
        if dist[now] < distance: continue
        for i in adj[now]:
            j = distance + i[1]
            if j < dist[i[0]]:
                dist[i[0]] = j
                heappush(q, (j, i[0]))
    
    return dist

# 지역 개수 /수색범위 /길 개수
n, m, r = map(int, input().split())
loot = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

ans = 0
for i in range(1, n + 1):
    temp = 0
    for num, d in enumerate(dijkstra(i)):
        if d <= m:
            temp += loot[num-1]
    ans = max(temp, ans)
            
print(ans)