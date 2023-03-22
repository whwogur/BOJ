# 21606 아침 산책
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    indoor = 0
    for i in adj[v]:
        if inout[i-1] == 0:
            if i not in visited:
                visited.add(i)
                indoor += dfs(i)
        
        else: indoor += 1

    return indoor
    
n = int(input().rstrip())
e = n - 1
inout = list(map(int,input().rstrip()))
adj = [[] for _ in range(n + 1)]
count = 0

for _ in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    if inout[a-1] == 1 and inout[b-1] == 1:
        count += 2 # 실내끼리 인접했을 경우 경로를 2개 더해준다

visited = set()
for i in range(1, n+1):
    indoor = 0
    if inout[i-1] == 0:
        if i not in visited:
            visited.add(i)
            indoor = dfs(i)

    count += indoor * (indoor-1)

print(count)
