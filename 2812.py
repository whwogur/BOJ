# 백준 2812
# 크게 만들기

N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()# 뺄 수 있는 숫자 수가 남아있고 스택.탑이 현재숫자보다
        k -= 1 # 작으면 팝, 뺄 수 있는 숫자 수 --
    stack.append(num[i]) # 현재 숫자 스택에 푸쉬

print(''.join(stack[:N-K]))