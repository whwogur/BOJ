# 11000 강의실 배정
from heapq import*
import sys

input = sys.stdin.readline
n = int(input().rstrip())
classes = sorted(list(map(int,input().split())) for _ in range(n))
h = [classes[0][1]]
for start, end in classes[1:]:
    if h[0] <= start:
        heappop(h)
    heappush(h,end)
print(len(h))