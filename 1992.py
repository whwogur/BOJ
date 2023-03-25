# 백준 1992
# 쿼드트리
# 조건이 만족하지않는경우( 색상이 모두 같지 않은 경우 ) 4개로 다시 쪼갠다.
# 시작하기 전 괄호'(' 를 넣고, 4개로 쪼개고 나서 각 처리를 다 하면 다시 ')
# 4개로 쪼개기 -> 재귀, 전달인자로 사분면 가장 왼쪽 위의 좌표와 크기
# 조건이 만족하는 경우(하나의 색상으로만 구성되는 경우) 해당 색상의 값을 출력
import sys
n = int(input())
video = [list(map(int, input())) for _ in range(n)]

def dfs(x, y, n):
    check = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != video[i][j]:
                check = -1
                break
    if check == -1:
        print('(', end='')
        n = n//2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)
        print(')',end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

dfs(0, 0, n)