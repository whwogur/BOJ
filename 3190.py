# 백준 3190
# 뱀
n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

board = [[0] * n for _ in range(n)] # 보드 초기화
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1 # 사과 위치 표시

l = int(input()) # 방향 변환 정보
changes = []
for _ in range(l):
    x, c = input().split()
    changes.append((int(x), c))

# 뱀의 초기 위치와 방향 설정
snake = [(0, 0)]
direction = 1 # 0: 위쪽, 1: 오른쪽, 2: 아래쪽, 3: 왼쪽

# 뱀의 이동
time = 0
idx = 0 # 다음에 회전할 방향 변환 정보의 인덱스
while True:
    time += 1
    row, col = snake[-1] # 뱀의 머리 위치
    if direction == 0:
        row -= 1
    elif direction == 1:
        col += 1
    elif direction == 2:
        row += 1
    else:
        col -= 1

    # 보드를 벗어나거나 자기 자신의 몸과 부딪히면 종료
    if row < 0 or row >= n or col < 0 or col >= n or (row, col) in snake:
        break

    snake.append((row, col))
    if board[row][col] == 1: # 사과를 먹으면
        board[row][col] = 0
    else: # 사과가 없으면
        snake.pop(0) # 꼬리 위치 비워줌

    # 방향 변환 시간이 되면 방향을 회전시킴
    if idx < l and time == changes[idx][0]:
        if changes[idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        idx += 1

print(time)
