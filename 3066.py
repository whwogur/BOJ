# 3066 브리징 시그널
import sys, bisect
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    arr = [int(input().rstrip()) for _ in range(n)]
    lis = [0]
    for i in arr:
        if i > lis[-1]:
            lis.append(i)
        else:
            lis[bisect.bisect_left(lis,i)] = i
    print(len(lis) - 1)