# 백준 18258
# 큐 2

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
q = deque()

def process_command(command):
    if command[0] == 'push':
        q.append(int(command[1]))

    elif command[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(q))
    
    elif command[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    
    elif command[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)

for _ in range(n):
    command = input().rstrip().split()
    process_command(command)