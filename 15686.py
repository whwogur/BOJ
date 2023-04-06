# 15686 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
n, m = map(int, input().split()) # n * n 도시
board = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
# 1 <= 집 개수 <= 2n
# m <= 치킨집 개수 <= 13
house_cnt = 0
chick_cnt = 0
houses = []
chicks = []
chick_dist = []
# idea -> 지도를 전부다 돌면서 집의 갯수, 치킨집 갯수, 좌표 정보를 모은다
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == 1:
            house_cnt += 1
            houses.append((i, j))
        elif board[i][j] == 2:
            chick_cnt += 1
            chicks.append((i, j))

answer = int(1e9)
for chick in combinations(chicks, m):
    tmp = 0
    for hx, hy in houses:
        shortest = int(1e9)
        for cx, cy in chicks:
            shortest = min(shortest, abs(hx - cx) + abs(hy - cy))
        tmp += shortest
    answer = min(answer, tmp)
print(answer)