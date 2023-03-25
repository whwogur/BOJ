# 3745 오름세
import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if not n:
        break
    n = int(n)
    arr = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    length = 1
    for x in arr[1:]:
        idx, start, end = 0, 0, length - 1
        while start <= end:
            mid = (start + end) // 2

            if dp[mid] < x:
                start = mid + 1
                idx = max(idx, mid + 1)
            else:
                end = mid - 1
        
        length = max(idx + 1, length)
        dp[idx] = x

    print(length)