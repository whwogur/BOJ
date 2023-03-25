# 백준 2512
# 이분탐색

from sys import stdin
input = stdin.readline

n = int(input().rstrip())
budget = list(map(int, input().rstrip().split()))
total = int(input().rstrip())

start, end = 0, max(budget)

while start <= end:
    mid = (start + end) // 2

    budget_addedup = 0 # 총 지출
    for i in budget:
        if i > mid:
            budget_addedup += mid
        else:
            budget_addedup += i
    if budget_addedup <= total: # 지출 양이 예산보다 작으면
        start = mid + 1
    else: # 지출 양이 예산보다 크면
        end = mid - 1
print(end)