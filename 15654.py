# N과 M 5
import sys

n,m= map(int,input().split())
 
s = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
a = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str,a)))
        return
    for i in range(n):
        if s[i] in a:
            continue
        a.append(s[i])
        dfs(depth + 1)
        a.pop()

dfs(0)