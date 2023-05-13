# 10974
n = int(input())
tmp = []

def recur():
    if len(tmp) == n:
        print(*tmp)
        return
    for i in range(1, n + 1):
        if i not in tmp:
            tmp.append(i)
            recur()
            tmp.pop()

recur()