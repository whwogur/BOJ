# 2550 전구
import sys
input = sys.stdin.readline

def lowerBound(list, num):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        if num <= list[mid]:
            high = mid
        elif num > list[mid]:
            low = mid + 1
    return high

n = int(input().rstrip())
buttons = list(map(int, input().split()))
bulbs = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

for i, bulb in enumerate(bulbs):
    dp[bulb] = i + 1

seq = []
idx = []

for i in buttons:
    now = dp[i]
    if len(seq) == 0 or seq[-1] < now:
        idx.append(len(seq))
        seq.append(now)
    else:
        current = lowerBound(seq, now)
        if len(seq) == current:
            seq.append(now)
        else:
            seq[current] = now
        idx.append(current)

print(len(seq))

answer = []
a = max(idx)
for bulb in idx[::-1]:
    n -= 1
    if a == bulb:
        answer.append(buttons[n])
        a -= 1

print(*sorted(answer))