# 주사위 굴리기
dice = [0, 
     0, 0, 0, 
        0, 
        0]
n, m, x, y, k = map(int ,input().split())

board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dx, dy = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0)

for command in commands:
    nx, ny = x + dx[command], y + dy[command]

    if not m > ny >= 0 <= nx < n: continue

    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if command == 1:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif command == 2:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif command == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    else:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[4])