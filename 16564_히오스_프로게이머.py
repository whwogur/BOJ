# 백준 16564
# 히오스 프로게이머

import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
levels = []

for i in range(n):
    levels.append(int(input().rstrip()))

# 이분탐색 시작
left = 1
right = k + max(levels)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total_up = sum(max(0, mid - level) for level in levels)

    if total_up <= k:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)

'''
위 코드에서 levels는 캐릭터들의 레벨을 담은 리스트입니다. 이분 탐색을 시작하기 전에, 이 리스트에서 가장 큰 값을 찾아서 이분 탐색의 끝점으로 설정합니다.
이분 탐색의 조건식에서는, 중간값인 mid를 설정한 후에, 이 mid를 목표로 하는 팀 목표레벨 T를 계산합니다.
이 때, max(0, mid - level)은 level보다 T가 큰 경우에만 레벨 업을 해야 하기 때문에, 이 값을 계산합니다.
이렇게 계산한 총합이 가능한 레벨 업의 총합 K 이하라면, 이 값이 가능한 최대 팀 목표레벨이 됩니다.
이 때, 이분 탐색의 시작점을 mid + 1로 설정하여 더 높은 팀 목표레벨을 찾습니다.
반면, 총합이 K보다 크다면, 이분 탐색의 끝점을 mid - 1로 설정하여 팀 목표레벨을 더 낮춥니다.
이렇게 이분 탐색을 반복하면서, 가능한 최대 팀 목표레벨 T를 찾을 수 있습니다.
'''



