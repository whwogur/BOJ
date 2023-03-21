# 2617 구슬찾기
import sys
input = sys.stdin.readline

# 문제에 주어진 연결관계를 통하여 특정 구슬의 하부 트리에 속하는 구슬 숫자 구하기
# 더 무거운 구슬 & 더 가벼운 구슬 그룹으로 나눈 후에 그래프 탐색, 특정 구슬보다
# 더 무거운 구슬의 갯수, 더 가벼운 구슬의 갯수 계산 후 (n + 1) /2 보다 크면
# 중간값은 될 수 없기 때문에 ++
def dfs(arr, n):
    global visited
    global check
    visited[n] = True
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            check += 1
            dfs(arr, i)

n, m = map(int, input().split())
heavierList = [[] for _ in range(n + 1)]
lighterList = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    heavierList[b].append(a)
    lighterList[a].append(b)

answer = 0
mid = (n+1) / 2
for i in range(1, n+1):
    visited = [False] * (n + 1)
    check = 0
    dfs(heavierList, i)
    if check >= mid:
        answer += 1
    check = 0
    dfs(lighterList, i)
    if check >= mid:
        answer += 1

print(answer)