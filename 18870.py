# 18870 좌표 압축

import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))

hl = sorted(list(set(nums)))
dic = {hl[i] : i for i in range(len(hl))}
for i in nums:
    print(dic[i], end = ' ')