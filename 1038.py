# 1038 감소하는 수
# 마지막 수는 마지막 앞자리 수 보다 작아야 한다
# 마지막 자리를 제외한 수도 무조건 감소하는 수가 되어야 한다
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]에서 만들수있는 감소하는 수는 2^10 - 1 => 1023
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input().rstrip())

result = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        result.append(int(num))

result.sort()
if n >= len(result):
    print(-1)
else:
    print(result[n])