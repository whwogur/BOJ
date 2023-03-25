# 백준 1715
# 카드 정렬하기

from heapq import*

n, *c=map(int,open(0))
heapify(c)
print(sum(heappush(c,x:=heappop(c)+heappop(c))or x for _ in c[1:]))

# lis = []
# for _ in c[1:]:
#     x = heappop(c) + heappop(c)
#     heappush(c, x)
#     lis.append(x)
# print(sum(lis))