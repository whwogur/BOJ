# 2490 윷놀이
for _ in range(3):
    a = list(map(int, input().split()))
    i = sum(a)
    if i == 4:
        print('E')
    elif i == 3:
        print('A')
    elif i == 2:
        print('B')
    elif i == 1:
        print('C')
    else:
        print('D')