# 11724 연결 요소의 개수
# DFS 돌면서 집합 체크
import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

def dfs(start):
    visited[start] = True

    for i in adj[start]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (1 + n)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        if not adj[i]:
            count += 1
            visited[i] = True
        else:
            dfs(i)
            count += 1

print(count)