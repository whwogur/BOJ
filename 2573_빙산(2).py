# 2573 빙산(BFS 풀이)
import sys
input = sys.stdin.readline
from collections import deque

def bfs(i, j, visited):
    q = deque([[i, j]])
    thaw_q = deque() # 빙하가 녹는 위치와 녹는 정도 저장
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        thaw_cnt = 0
        for dx, dy in direction:
            nx = i + dx
            ny = j + dy
            if y-1 >= ny >= 0 <= nx <= x-1 and visited[nx][ny] == 0:
                # 빙산의 높이가 있고 방문을 안했을 경우 enqueue
                if glacier[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                else:
                    thaw_cnt += 1
        if thaw_cnt:
            thaw_q.append([i, j, thaw_cnt])
    return thaw_q


x, y = map(int, input().rstrip().split())
glacier = [[int(n) for n in input().split()] for _ in range(x)]
direction = ((1,0), (-1,0), (0, -1), (0, 1))

years = 0
# 반복문 종료 조건 -> 빙산이 전부 녹았거나, 2구역 이상으로 나눠졌을 경우
while True:
    cnt = 0
    visited = [[0 for _ in range(y)] for _ in range(x)]
    for i in range(x - 1):
        for j in range(y - 1):
            if glacier[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                thaw = bfs(i, j, visited) # bfs > 각 좌표별 녹는정도 반환
                while thaw:
                    tx, ty, t = thaw.popleft()
                    glacier[tx][ty] = max(glacier[tx][ty] - t, 0)
    if cnt == 0:
        years = 0
        break
    if cnt >= 2:
        break
    years += 1

print(years)