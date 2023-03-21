# 1432 그래프 수정
import sys
from heapq import*
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
outDegree = [0] * (n + 1)
result = [0] * (n + 1)

for i in range(1, n+1):
    relation = list(map(int, input().rstrip()))

    for idx, val in enumerate(relation):
        if val == 1:
            graph[idx + 1].append(i)
            outDegree[i] += 1

# 위상 정렬
def topologicalSort(n):
    heap = []

    # 차수 0인 노드 큐에 삽입
    for i in range(1, n+1):
        if outDegree[i] == 0:
            heappush(heap, -i)

    while heap:
        # 우선순위 큐를 이용하여 큐에서 인덱스가 가장 큰 노드 꺼냄
        now = -heappop(heap)
        result[now] = n

        for related_node in graph[now]:
            outDegree[related_node] -= 1
            if outDegree[related_node] == 0:
                heappush(heap, -related_node)

        n -= 1

topologicalSort(n)

if result.count(0) > 2:
    print(-1)
else:
    print(' '.join(map(str, result[1:])))
