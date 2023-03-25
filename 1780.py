# 백준 1780

from sys import stdin
input = stdin.readline

def recursion(row, col, n):
    current = paper[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            if paper[i][j] != current:
                # 종이 9등분
                _n = n // 3
                recursion(row, col, _n)
                recursion(row, col+_n, _n)
                recursion(row, col+(_n*2), _n)
                recursion(row+_n, col, _n)
                recursion(row+_n, col+_n, _n)
                recursion(row+_n, col+(_n*2), _n)
                recursion(row+(_n*2), col, _n)
                recursion(row+(_n*2),col+_n, _n)
                recursion(row+(_n*2),col+(_n*2),_n)
                return
            
    result[str(current)] += 1
    return

n = int(input().rstrip())
paper = []
for _ in range(n):
    row = list(map(int, input().rstrip().split()))
    paper.append(row)

result = {'-1':0, '0':0, '1':0}

recursion(0, 0, n)

for i in result.values():
    print(i)