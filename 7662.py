# 7662 이중 우선순위 큐
import sys
from heapq import*
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    k = int(input().rstrip())
    q1, q2 = [], []
    visited = [False for _ in range(k)]
    for i in range(k):
        command, num = input().split()
        if command == 'I':
            heappush(q1, (int(num), i))
            heappush(q2, (-int(num), i))
            visited[i] = True
        else:
            if num == '1':
                while q2 and not visited[q2[0][1]]:
                    heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heappop(q2)
            else:
                while q1 and not visited[q1[0][1]]:
                    heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heappop(q1)

    while q1 and not visited[q1[0][1]]:
        heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heappop(q2)
    
    if not q1 or not q2:
        print('EMPTY')
    else:
        print(-q2[0][0], q1[0][0])