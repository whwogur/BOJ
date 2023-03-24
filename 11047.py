# 11047 동전0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(n)]
coins.sort(reverse=True)
idx = 0
cnt = 0
while k > 0:
    cnt += k // coins[idx]
    k %= coins[idx]
    idx += 1

print(cnt)