# 2637 장난감조립
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
adj = [[] for _ in range(n + 1)]
parts_needed = [[0] * (n + 1) for _ in range(n + 1)]
q = deque()
degree = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[b].append((a,c))
    degree[a] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지
    for next, next_parts_needed in adj[now]:
        # 만약 현 제품이 기본 부품이면
        if parts_needed[now].count(0) == n + 1:
            parts_needed[next][now] += next_parts_needed
        # 현 제품이 중간 제품이면
        else:
            for i in range(1, n + 1):
                parts_needed[next][i] += parts_needed[now][i] * next_parts_needed

        # 차수 - 1
        degree[next] -= 1
        if degree[next] == 0:
            # 차수 0아면 큐에 넣음
            q.append(next)

for parts in enumerate(parts_needed[n]):
    if parts[1] > 0:
        print(*parts)