# 1766 문제집
import sys
from heapq import*
input = sys.stdin.readline

n, m = map(int, input().split())
degrees = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
q = []
answer = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degrees[b] += 1

for i in range(1, n + 1):
    if degrees[i] == 0:
        heappush(q,i)

while q:
    tmp = heappop(q)
    answer.append(tmp)
    for i in graph[tmp]:
        degrees[i] -= 1
        if degrees[i] == 0:
            heappush(q,i)

print(*answer)