# 11725
# DFS 하면서 부모가 없으면 설정해준다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, adj, parents):
    for i in adj[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, adj, parents)

n = int(input().rstrip())
adj = [[] for _ in range(n + 1)]
parents = [0] * (n+1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1, adj, parents)

for i in range(2, n+1):
    print(parents[i])