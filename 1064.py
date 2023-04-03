# 1094 막대기
import sys
input = sys.stdin.readline

x = int(input().rstrip())
cnt = 0
while x != 0:
    if x % 2 == 1:
        cnt += 1
    x //= 2
print(cnt)