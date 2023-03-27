# LCS 4
import sys
input = sys.stdin.readline

def lowerBound(list, num):
    low, high = 0, len(list) - 1
    while low < high:
        mid = (low + high) // 2
        if list[mid] < num:
            low = mid + 1
        elif list[mid] >= num:
            high = mid
    return high

n = int(input().rstrip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dic_a = dict().fromkeys([i for i in range(n + 1)], -1)
dic_b = dict().fromkeys([i for i in range(n + 1)], -1)

for i in range(n):
    dic_a[a[i]] = i
    dic_b[b[i]] = i

arr = []
for i in range(n):
    arr.append(dic_b[a[i]])

lis = []
for i in range(n):
    if not lis:
        lis.append(arr[i])
    else:
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            lis[lowerBound(lis,arr[i])] = arr[i]
print(len(lis))