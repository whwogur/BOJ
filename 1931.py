# 1931 회의실 배정

import sys
input = sys.stdin.readline
n = int(input().rstrip())

meetings = []

for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))

meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = 0
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1
print(answer)