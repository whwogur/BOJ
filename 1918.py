# 백준 1918
# 스택
import sys
input = sys.stdin.readline

def postfix(expression):
    stack = []

    for i in range(len(expression)):
        if 'A' <= expression[i] <= 'Z':
            print(expression[i], end='')
        elif (expression[i] == '+' or expression[i] == '-'):
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(expression[i])
        elif expression[i] == '*' or expression[i] == '/':
            while stack and stack[-1] != '(' and (stack[-1] =='*' or stack[-1] == '/'):
                print(stack.pop(), end='')
            stack.append(expression[i])
        elif expression[i] == '(':
            stack.append(expression[i])
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()

    if len(stack) > 0:
        for i in range(len(stack)):
            print(stack.pop(), end='')

expression = input().rstrip()
postfix(expression)
