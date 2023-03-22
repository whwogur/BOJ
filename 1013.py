# 1013 Contact
import re
import sys
input = sys.stdin.readline

T = int(input().rstrip())
answer = []

for _ in range(T):
    signal = input().replace('\n', '')
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(signal)
    if m: answer.append('YES')
    else: answer.append('NO')

print(*answer, sep='\n')