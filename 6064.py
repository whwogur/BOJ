# 6064 카잉 달력
import sys
input = sys.stdin.readline

def cal(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

for i in range(int(input().rstrip())):
    m, n, x, y = map(int, input().split())
    print(cal(m, n, x, y))