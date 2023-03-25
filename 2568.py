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

cables = []
dic = {}
lis = [-1]
answer = []
traceBack = []
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


    # 1 8
    # 2 2
    # 3 9
    # 4 1
    # 6 4
    # 7 6
    # 9 7
    # 10 10
'''
반례
4
1 2
2 3
3 4
4 1

답
1
4

오답
1
1
'''