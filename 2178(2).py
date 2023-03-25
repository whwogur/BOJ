# 백준 2178
# 미로탐색
# BFS 이용 해결
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x, y))
    # 큐가 빌때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    # 가장 오른쪽 아래까지(n, m)의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS 결과 출력
print(bfs(0,0))