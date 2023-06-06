# 17266 어두운 굴다리
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
lights = list(map(int, input().split()))
lights_cnt = len(lights)

min_height = 0

if lights_cnt == 1:
    min_height = max(lights[0] - 0, n - lights[0])
else:
    for i in range(lights_cnt):
        if i == 0:
            height = lights[i] - 0
        elif i == lights_cnt - 1:
            height = n - lights[i]
        else:
            tmp = lights[i] - lights[i - 1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2
        min_height = max(height, min_height)

print(min_height)