# 9249 최장 공통 부분 문자열
import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
s = a + '$' + b
n = len(s)
sa = [i for i in range(n)]
pos = [ord(s[i]) for i in range(n)] + [-1]
d = 1
while True:
    sa.sort(key=lambda x: (pos[x], pos[min(x + d, n)]))
    tmp = [0] * n
    for i in range(n - 1):
        x, y = sa[i], sa[i + 1]
        tmp[i + 1] = tmp[i] + ((pos[x], pos[min(x + d, n)]) < (pos[y], pos[min(y + d, n)]))
    
    for i in range(n):
        pos[sa[i]] = tmp[i]
    
    if tmp[-1] == n - 1:
        break
    
    d *= 2

lcp = [0] * n
k = 0
idx = 0
maxi = 0
for i in range(n):
    if pos[i] == 0:
        k -= (k > 0)
        continue
    
    j = sa[pos[i] - 1]
    while (max(i, j) + k < n) and (s[i + k] == s[j + k]) and (min(i, j) < len(a) - k < max(i, j)):
        k += 1
    
    lcp[pos[i]] = k
    if maxi < k:
        maxi = k
        idx = i
    
    k -= (k > 0)

print(maxi)
print(s[idx:idx + maxi])