# 1789 수들의 합
a = int(input())
n = 1
while n * (n + 1) / 2 <= a:
    n += 1
print(n - 1)