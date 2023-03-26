# 1149 RGB거리
import sys
input = sys.stdin.readline

n = int(input().rstrip())
paint = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    paint[i][0] = min(paint[i - 1][1], paint[i - 1][2]) + paint[i][0]
    paint[i][1] = min(paint[i - 1][0], paint[i - 1][2]) + paint[i][1]
    paint[i][2] = min(paint[i - 1][0], paint[i - 1][1]) + paint[i][2]
print(min(paint[n-1][0], paint[n-1][1], paint[n-1][2]))