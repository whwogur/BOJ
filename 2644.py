# 2644 촌수계산
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
n = int(input().rstrip())
start, end = map(int, input().split())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, cnt):
    cnt += 1
    visited[start] = True
    
    if start == end:
        result.append(cnt)
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i, cnt)

dfs(start, -1)
print(result[0] if len(result)!=0 else -1)