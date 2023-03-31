# 1693 트리 색칠하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(idx):
    for i in s[idx]:
        if visited[i]:
            continue
        visited[i] = True
        dfs(i)
        for j in range(1, 17):
            m_num = 100000000
            for k in range(1, 17):
                if j != k:
                    if m_num > memo[i][k]:
                        m_num = memo[i][k]
            memo[idx][j] += m_num
    for i in range(1, 17):
        memo[idx][i] += i
    return

n = int(input().rstrip())
s = [[] for _ in range(n + 1)]
memo = [[0] * 17 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)
visited[1] = True
dfs(1)
print(min(memo[1][1:]))