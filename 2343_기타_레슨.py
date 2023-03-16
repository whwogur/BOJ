# 백준 2343
# 이분탐색
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lect = list(map(int, input().rstrip().split()))

maxlen = max(lect)
start, end = maxlen, sum(lect)
answer = 1e9

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    tmp = 0
    for i in range(n):
        if(tmp + lect[i] <= mid):
            # 만약 현재 블루레이에 강의를 더 넣을 수 있다면
            tmp += lect[i]
        else:
            cnt += 1
            tmp = lect[i]
        if cnt > m:
            break
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        if mid >= maxlen: # 최솟값을 찾기 위해 값을 비교할때 리스트의
            answer = min(answer, mid) #최대값보다 작으면 결과값에 안넣음

print(answer)
