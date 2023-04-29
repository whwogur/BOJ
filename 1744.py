# 1744 수 묶기
n = int(input())
pos = []
neg = []

result = 0
for i in range(n):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num <= 0:
        neg.append(num)
    else:
        result += num

pos.sort(reverse=True)
neg.sort()

for i in range(0, len(pos), 2):
    if i+1 >= len(pos):
        result += pos[i]
    else:
        result += (pos[i] * pos[i+1])

for i in range(0, len(neg), 2):
    if i+1 >= len(neg):
        result += neg[i]
    else:
        result += (neg[i] * neg[i+1])

print(result)