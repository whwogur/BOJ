# 백준 2805
# 나무 자르기

import sys
input = sys.stdin.readline

def binarySearch(trees, start, end):
    result = 0
    while start <= end: # 시작점이 끝점보다 클때까지 반복한다
        mid = (start + end) // 2 # 중간은 양끝 값의 평균
        _total = 0 # 가져갈수있는 나무

        for tree in trees: # 나무 하나씩 탐색
            if tree > mid: # 나무 크기가 중간값보다 크면
                _total += tree - mid # 나무 크기 - 중간값(톱의 위치) -> 잘린 크기 만큼 가져갈 나무에 추가한다
        
        if _total < M: # 잘린 나무가 목표량보다 적으면
            end = mid -1 # (끝값 = 중간값-1 이 된다 -> 다음 while문에 톱 더 낮아짐)
        else: 
            result = mid
            start = mid + 1
    return result

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

ans = binarySearch(trees, 0, max(trees))
print(ans)

# while문 돌면서 중간값을 구해주고 중간값을 나무 자르는 높이로 생각 했을때
# 나무길이 리스트에서 나무 한개씩 가져와 자르는 높이보다 크면
# 나무를 잘라서 total에 더함

# 나무가 M 만큼 필요한데 total이 M보다 작으면 나무가 더 필요하므로 end값을 mid-1로
# (end값을 기존보다 작게 함으로써 mid가 값이 작아지면 total 값은 증가)
