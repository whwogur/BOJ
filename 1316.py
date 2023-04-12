# 1316 그룹 단어 체커
import sys
input = sys.stdin.readline
n = int(input())
cnt = n
for _ in range(n):
    word = list(input().rstrip())
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            cnt -= 1
            break
print(cnt)