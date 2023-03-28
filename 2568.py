# 2568 전깃줄 2
import sys
input = sys.stdin.readline

def lowerBound(list, num):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        if num <= list[mid]:
            high = mid
        elif num > list[mid]:
            low = mid + 1
    return high

n = int(input().rstrip())
cables = []
dic = {}
lis = [-1]
answer = []
traceBack = []

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
    answer.append(lis.index(i) + 1)

lisLength = len(lis)
for i in range(len(cables)-1, -1, -1):
    if answer[i] == lisLength:
        traceBack.append(cables[i])
        lisLength -= 1

print(n - (len(lis) -1))
cables.sort()
for i in traceBack:
    cables.remove(i)
for i in cables:
    print(i)