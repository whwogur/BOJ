# 1011 Fly me to the Alpha Centauri
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    count = 0
    move = 1
    move_sum = 0
    while move_sum < distance:
        count += 1
        move_sum += move
        if count % 2 == 0:
            move += 1
    print(count)