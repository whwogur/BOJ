# 백준 5639
import sys
# 전위 순회를 했으므로 루트 노드보다 큰 원소가 나오는 지점이 왼쪽 서브트리를
# 나누는 지점과 같다.

def dfs(start, end):

    # 시작과 끝 값이 역전시 리턴
    if start > end:
        return
    temp = end + 1
    # 만약 모든 원소가 루트 노드보다 작은 경우
    # start +1, end 삽입, 즉 루트 노드를 제외한 트리
    # dfs(temp, end): end + 1, end가 삽입되어 if start > end
    # 에의해 리턴됨 -> 오른쪽 노드가 없음을 의미

    # 서브 트리 찾기
    for i in range(start + 1, end + 1):
        # 루트 보다 크면 오른쪽 서브 트리
        if graph[start] < graph[i]:
            temp = i
            break

    dfs(start + 1, temp - 1) # 왼쪽 서브 트리 재귀적으로 탐색
    dfs(temp, end) # 오른쪽 서브 트리 재귀적으로 탐색

    print(graph[start])

graph = []
while True:
    try:
        graph.append(int(sys.stdin.readline()))
    except:
        break

dfs(0, len(graph) - 1)