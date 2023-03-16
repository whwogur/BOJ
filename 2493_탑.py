# 백준 2493
import sys
input = sys.stdin.readline

n = int(input().rstrip())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
check = [0] * n

for i in range(n): # 타워를 하나씩 본다
    t = tower[i]
    while stack and tower[stack[-1]] < t: # 스택의 탑보다 현재 타워가
        stack.pop() # 크면 계속 팝
    if stack: # 스택이 남았으면 
        check[i] = stack[-1] + 1 # 현재 타워의 신호를 받는 타워의 인덱스 체크
    stack.append(i) # 현재 타워의 인덱스 스택에 푸쉬

print(*check, sep=' ')