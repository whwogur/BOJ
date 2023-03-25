# 백준 17608
# 막대기

import sys
input = sys.stdin.readline

n = int(input())
sticks = []

result = 1

for _ in range(n):
    sticks.append(int(input().rstrip()))

max = sticks[-1]

for i in range(len(sticks)-1, -1, -1):
    if sticks[i] > max:
        result += 1
        max = sticks[i]

print(result)
    