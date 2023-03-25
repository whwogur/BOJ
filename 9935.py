# 백준 9935
# 스택
import sys
input = sys.stdin.readline

string = input().rstrip()
explosive = input().rstrip()

stack = []
exp_len = len(explosive)

for i in range(len(string)):
    stack.append(string[i])
    a = ''.join(stack[-exp_len:])
    if ''.join(stack[-exp_len:]) == explosive:
        for _ in range(exp_len):
            stack.pop()

if stack:
    print(*stack,sep='')
else:
    print('FRULA')