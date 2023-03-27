# 1202 보석도둑
import sys
from heapq import*
input = sys.stdin.readline

n, k = map(int, input().split())
jwlry = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input().rstrip()) for _ in range(k)]
jwlry.sort() # weight value
bags.sort()

tmp = []
answer = 0

for bag in bags:
    while jwlry and bag >= jwlry[0][0]:
        heappush(tmp, -jwlry[0][1])
        heappop(jwlry)
    if tmp:
        answer += heappop(tmp)
    elif not jwlry:
        break

print(-answer)
