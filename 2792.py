import sys, math
input = sys.stdin.readline
N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]
left,right = 1,max(colors)
ans = 1e9
while True:
    if left > right:
        break

    m = (left+right)//2
    tmp = 0
    for i in colors:
        tmp += math.ceil(i/m)
    if tmp > N:
        left = m+1
    else:
        right = m-1
        ans = min(ans, m)

print(ans)