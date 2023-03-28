# 2565 전깃줄
import sys
input = sys.stdin.readline
def lowerBound(list, num):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        if list[mid] > num:
            high = mid
        elif list[mid] <= num:
            low = mid + 1
    return high

lis = [-1]
cables = []
dic = {}
n = int(input().rstrip())
for _ in range(n):
    a, b = map(int, input().split())
    dic[b] = a
temp = sorted(dic)
for i in temp:
    cables.append(dic.get(i))
for i in cables:
    if i > lis[-1]:
        lis.append(i)
    else:
        lis[lowerBound(lis, i)] = i

print(n - (len(lis) - 1))