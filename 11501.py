# 주식
import sys
input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    stock = list(map(int, input().split()))
    stock.reverse()
    max = stock[0]
    sum = 0

    for i in range(1, n):
        if max < stock[i]:
            max = stock[i]
            continue
        sum += max - stock[i]
    print(sum)