# 1916 최소비용 구하기
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 입력
n = int(input().rstrip()) # 노드개수
m = int(input().rstrip()) # 간선개수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # (도착지,비용)
start, dest = map(int, input().split())
# 다익스트라
def dijkstra(graph, start):
    fare = [INF] * (n+1)
    fare[start] = 0
    queue = []
    heapq.heappush(queue, [fare[start], start])  # 시작 노드부터 탐색 시작

    while queue:
        _cost, node = heapq.heappop(queue)

        if fare[node] < _cost:
            continue

        for next_node, next__cost in graph[node]:
            total_cost = _cost + next__cost  # 인접노드까지의 값
            if total_cost < fare[next_node]:  # 기존 값보다 싸면 갱신
                fare[next_node] = total_cost
                heapq.heappush(queue, [total_cost, next_node])  # 다음 노드까지 값 계산하기위해 삽입
    return fare
#출력
cheapest = dijkstra(graph, start)
print(cheapest[dest])