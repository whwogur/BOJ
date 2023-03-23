# 1967 트리의 지름
import sys
input = sys.stdin.readline

def dfs(x, length):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = length + b
            dfs(a, length + b)

n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
