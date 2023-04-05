# 14226 이모티콘
from collections import deque
S = int(input())
q = deque()
q.append((1, 0))
visited = dict()
visited[(1, 0)] = 0

while q:
    now, clip = q.popleft()
    if now == S:
        print(visited[(now, clip)])
        break
    # 이모티콘 모두 복사
    if (now, now) not in visited.keys():
        visited[(now, now)] = visited[(now, clip)] + 1
        q.append((now, now))
    # 클립보드에 있는 이모티콘 붙여넣기
    if (now + clip, clip) not in visited.keys():
        visited[(now + clip, clip)] = visited[(now, clip)] + 1
        q.append((now + clip, clip))
    # 화면의 이모티콘 하나 삭제
    if (now - 1, clip) not in visited.keys():
        visited[(now - 1, clip)] = visited[(now, clip)] + 1
        q.append((now - 1, clip))