# 1005 ACM Craft
import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n, k = map(int, input().split())
    buildTime = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1
    cons2Win = int(input().rstrip())

    q = deque()
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = buildTime[i]
    
    while q:
        a = q.popleft()
        for i in graph[a]:
            inDegree[i] -= 1
            dp[i] = max(dp[a] + buildTime[i], dp[i])
            if inDegree[i] == 0:
                q.append(i)

    
    print(dp[cons2Win])