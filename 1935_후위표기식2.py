# 백준 1935
# 스택
import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = list(input().rstrip())
# 피연산자가 나오면 stack에 푸쉬, 연산자가 나오면 pop
# 단 stack에서 피연산자를 pop할 때, '-'연산이나 '/'연산은 순서가
# 유지되어야 하기 때문에 먼저 pop한 값을 alphabet_2에 저장해주고 alphabet_1 alphabet_2순
# 으로 계산해준다. 출력 시 소수점 둘째자리까지 나오게 해야한다
chars = [0] + list(int(input().rstrip()) for _ in range(n))

stack = []

for letter in string:
    if 'A' <= letter <= 'Z':
        stack.append(chars[ord(letter) - ord('A') + 1])
    else:
        alphabet_2 = stack.pop()
        alphabet_1 = stack.pop()

        if letter == '+':
            stack.append(alphabet_1 + alphabet_2)
        elif letter == '-':
            stack.append(alphabet_1 - alphabet_2)
        elif letter == '*':
            stack.append(alphabet_1 * alphabet_2)
        else:
            stack.append(alphabet_1 / alphabet_2)

print("%.2f" %stack[0])