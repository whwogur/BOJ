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
    dic[b] = a # b 전봇대 : a 전봇대
temp = sorted(dic) # 키값(b전봇대)을 sorted list로
for i in temp:
    cables.append(dic.get(i)) # cables = [4, 2, 6, 7, 9, 1, 3, 10]
for i in cables: # cables 에서 LIS 길이 찾기
    if i > lis[-1]:
        lis.append(i)
    else:
        lis[lowerBound(lis, i)] = i

print(n - (len(lis) - 1))