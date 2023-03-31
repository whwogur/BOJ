# 11441 합 구하기
import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
mem = [nums[0]]
for i in range(1, n):
    mem.append(mem[-1] + nums[i])
for _ in range(int(input().rstrip())):
    start, end = map(int, input().split())
    if start == 1:
        print(mem[end - 1])
    else:
        print(mem[end - 1] - mem[start - 2])