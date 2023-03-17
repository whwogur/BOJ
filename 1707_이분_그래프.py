import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        x = q.popleft()
        for i in adj[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                q.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True

k = int(input().rstrip()) # 테스트 케이스
for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    flag = True

    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    for i in range(1, v+1):
        if visited[i] == 0:
            if not bfs(i):
                flag = False
                break
    
    print('YES' if flag == 1 else 'NO')