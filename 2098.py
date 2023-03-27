# 2098 외판원 순회
import sys
input = sys.stdin.readline
INF = int(1e9)
# dp[cur][visited] = min(dp[cur][visited], dp[next][visited | (1 << next)] + graph[cur][next])

def recursion(x, visited):
    if visited == (1 << n)-1:
        if graph[x][0] == 0:
            return INF
        dp[x][visited] = graph[x][0]
        return graph[x][0]
    
    if dp[x][visited] != -1:
        return dp[x][visited]
    
    min_cost = INF
    for i in range(n):
        # if not visited i node yet && graph != 0
        if not visited & (1 << i) and graph[x][i] != 0:
            min_cost = min(min_cost, graph[x][i] + recursion(i, visited | (1 << i)))
    
    dp[x][visited] = min_cost
    return min_cost

n = int(input().rstrip())
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(recursion(0, 1))