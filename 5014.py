# 5014 스타트링크
import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [False for _ in range(f + 1)]
cnt = [0 for _ in range(f + 1)]

q = deque()
q.append(s)
visited[s] = True
while q:
    now = q.popleft()
    if now == g:
        break
    for nf in (now + u, now - d):
        if 0 < nf <= f and not visited[nf]:
            q.append(nf)
            cnt[nf] = cnt[now] + 1

if not visited[g]:
    print('use the stairs')
else:
    print(cnt[g])