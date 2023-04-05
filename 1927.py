# 1927 최소 힙
from heapq import*
import sys
input = sys.stdin.readline

q = []
for _ in range(int(input().rstrip())):
    a = int(input().rstrip())
    if a > 0:
        heappush(q, a)
    elif a == 0:
        if q:
            print(heappop(q))
        else:
            print(0)