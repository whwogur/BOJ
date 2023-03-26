# 1516 게임개발
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
indegree = [0]*(n+1)
arr = [[0]*(n+1) for _ in range(n+1)]
time = [0]*(n+1)

for i in range(1, n+1):
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    for x in _input[1:-1]:
        arr[i][x] = 1
        indegree[i] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    t = 0
    for i in range(1, n+1):
        if arr[i][x] == 1:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        if arr[x][i] == 1:
            t = max(time[i], t)
    time[x] += t

for i in time[1:]:
    print(i)