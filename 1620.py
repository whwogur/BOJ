# 1620 포켓몬마스터이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poke = dict()
for i in range(1, n + 1):
    a = input().rstrip()
    poke[i] = a
    poke[a] = i

for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(poke[int(q)])
    else:
        print(poke[q])