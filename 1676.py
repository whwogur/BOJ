# 1676 팩토리얼 0의 개수
from math import factorial

n = int(input())
cnt = 0
for i in str(factorial(n))[::-1]:
    if i != '0':
        break
    cnt += 1
print(cnt)