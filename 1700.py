# 1700 멀티탭 스케줄링
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = list(map(int, input().split()))
plugs = []
count = 0

for i in range(k):
    # 다음에 쓸 것이면 건너뛴다
    if sequence[i] in plugs:
        continue
    # 플러그가 1개라도 비어있으면 꽂는다
    if len(plugs) < n:
        plugs.append(sequence[i])
        continue

    idxs = [] # 다음 멀티탭 값 저장
    hasplug = True

    for j in range(n):
        # 멀티탭 안에 플러그 값이 있으면
        if plugs[j] in sequence[i:]:
            # 멀티탭 인덱스 위치 가져온다
            idx = sequence[i:].index(plugs[j]) ###
        else:
            idx = 101
            hasplug= False
        # 인덱스에 값을 넣어준다
        idxs.append(idx)
        # 없다면 종료
        if not hasplug:
            break
    # 플러그를 뽑는다
    plug_out = idxs.index(max(idxs))
    del plugs[plug_out] # 플러그에서 제거
    plugs.append(sequence[i]) # 플러그에 멀티탭 값 삽입
    count += 1 # 뽑은 카운트 증가

print(count)
