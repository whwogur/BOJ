# 2217 로프
import sys
input = sys.stdin.readline

n = int(input().rstrip())
ropes = [int(input().rstrip()) for _ in range(n)]
ropes.sort(reverse=True)
answer = []

for j in range(n):
    answer.append(ropes[j]*(j + 1))
print(max(answer))