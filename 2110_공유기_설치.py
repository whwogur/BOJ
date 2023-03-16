# 백준 2110
# 공유기 설치

import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(N)]
arr.sort()

start, end = 1, arr[N-1] - arr[0]
answer = 0

if C == 2:
    print(arr[N-1] - arr[0])
else:
    while(start < end):
        mid = (start + end) // 2

        cnt = 1
        a = arr[0]
        # 마지막으로 설치된 공유기 위치
        for i in range(N):
            if arr[i] - a >= mid:
                cnt += 1
                a = arr[i]
        if cnt >= C:
            answer = mid
            start = mid + 1
        elif cnt < C:
            end = mid
    print(answer)