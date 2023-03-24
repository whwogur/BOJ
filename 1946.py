# 1946 신입사원
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    app = list(tuple(map(int, input().split())) for _ in range(n))
    app.sort(key=lambda x: x[0])
    a = n + 1
    answer = 0
    for i in app:
        if i[1] <= a:
            answer += 1
            a = i[1]

    print(answer)