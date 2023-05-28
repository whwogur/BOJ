# 2720 세탁소 사장 동혁
coins = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    n = int(input())
    answer = [0, 0, 0, 0]
    for i in range(4):
        answer[i] = n // coins[i]
        n %= coins[i]
    print(*answer, sep=' ')