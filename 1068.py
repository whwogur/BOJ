# 1068 트리
import sys
input = sys.stdin.readline

def dfs(rid, nodes):
    nodes[rid] = 'X'
    for i in range(len(nodes)):
        if rid == nodes[i]:
            dfs(i, nodes)

n = int(input())
nodes = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
rid = int(input().rstrip())

answer = 0
dfs(rid, nodes)
for i in range(len(nodes)):
    if nodes[i] != 'X' and i not in nodes:
        answer += 1
print(answer)