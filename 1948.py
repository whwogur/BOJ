# 1948 임계경로
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

time = [0] * (n + 1)
inDegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]
cnt = [[] for _ in range(n + 1)]

for _ in range(m):
    # a: 출발 도시, b : 도착 도시, c: 걸리는 시간
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    rev_graph[b].append(a)
    inDegree[b] += 1

start, dest = map(int, input().split())

q = deque([])
# 도시, 지나온 경로 개수
q.append(start)

while q:
    # now: 도시, c: 지나온 경로의 개수
    now = q.popleft()
    # i[0]: 비용, i[1]: 도시
    for i in graph[now]:
        inDegree[i[1]] -= 1
        # 비용이 갱신 될 때
        if time[i[1]] < time[now] + i[0]:
            time[i[1]] = time[now] + i[0]
            # 달려야 하는 도로의 수 갱신
            cnt[i[1]] = [now]
        elif time[i[1]] == time[now] + i[0]:
            cnt[i[1]].append(now)

        # 선행 도로를 모두 지나갔을 때
        if inDegree[i[1]] == 0:
            q.append(i[1])

q = deque([dest])
route = set()
while q:
    now = q.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(time[dest])
print(len(route))