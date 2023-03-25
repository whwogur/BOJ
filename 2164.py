# 백준 2164
# 카드2

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
q = deque([i for i in range(1, n+1)])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
    
print(q.pop())
