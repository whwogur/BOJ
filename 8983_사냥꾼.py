# 백준 8983
# 사냥꾼

import sys
import bisect
input = sys.stdin.readline

m, n, l = map(int, input().rstrip().split())
stands = sorted(map(int, input().rstrip().split()))
monsters = [tuple(map(int, input().rstrip().split())) for _ in range(n)]

catchable = 0

for monster_pos in monsters:
    x, y = monster_pos

    left_idx = bisect.bisect_left(stands, x - l + y)
    right_idx = bisect.bisect_right(stands, x + l - y)

    for i in range(left_idx, right_idx):
        _stand = stands[i]
        if abs(_stand - x) + y <= l:
            catchable += 1
            break

print(catchable)

'''
첫 번째로, 사대 위치를 기준으로 왼쪽에 위치한 동물들과 오른쪽에 위치한 동물들을 분류합니다.
이를 위해서 각 동물의 위치와 사대의 위치를 비교해서 거리가 L 이하인 동물을 잡을 수 있습니다.
거리를 계산할 때는 동물의 y좌표를 고려해야 하므로, 각 동물의 x, y 좌표와 사대의 x좌표를 이용해 거리를 계산합니다.

두 번째로, 왼쪽에 위치한 동물들 중에서 가장 오른쪽에 있는 동물과 오른쪽에 위치한 동물들 중에서 가장 왼쪽에 있는 동물을 찾아야 합니다.
이를 위해서 각 동물들을 x 좌표를 기준으로 오름차순으로 정렬하고, 왼쪽 동물들 중에서 가장 오른쪽에 있는 동물과 오른쪽 동물들 중에서 가장 왼쪽에 있는 동물을 찾습니다.

세 번째로, 왼쪽 동물들과 오른쪽 동물들을 각각 하나씩 선택해서 잡을 수 있는지 확인합니다.
이를 위해서 왼쪽 동물들은 가장 오른쪽에 있는 동물부터 시작해서 오른쪽 동물들은 가장 왼쪽에 있는 동물부터 시작해서 하나씩 선택합니다.
선택한 동물과 사대의 거리가 L 이하인 경우에는 잡을 수 있으므로, 선택한 동물의 수를 증가시킵니다.

마지막으로, 잡을 수 있는 동물의 수를 출력합니다.
'''