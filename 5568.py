# 백준 5568번
# 카드 놓기
# 같은 숫자가 생기는 경우를 대비해서 set 이용

from itertools import permutations
import sys
input = sys.stdin.readline

n, k = int(input()), int(input())
cards = [input().rstrip() for i in range(n)]
res = set()

for permutation in permutations(cards, k):
    res.add(''.join(permutation))

print(len(res))

