# 7795 먹을 것인가 먹힐 것인가
import sys
input = sys.stdin.readline
def lowerbound(list, num):
    low = 0
    high = len(list)
    while low < high:
        mid = (high + low) // 2
        if list[mid] < num:
            low = mid + 1
        elif list[mid] >= num:
            high = mid
    return high
for _ in range(int(input().rstrip())):
    n, m = map(int,input().split())
    ans = 0
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    for A in a:
        ans += lowerbound(b, A)
    print(ans)
