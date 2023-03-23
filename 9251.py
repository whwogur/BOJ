# 9251 LCS
import sys
input = sys.stdin.readline
MAXLEN = 1001

word1, word2 = input().rstrip(), input().rstrip()
l_1, l_2 = len(word1), len(word2)
cache = [0] * MAXLEN

for i in range(l_1):
    cnt = 0
    for j in range(l_2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))