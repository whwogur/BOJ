# 백준 2628번
# 종이자르기
# 가로 번호 -> 세로 길이
# 세로 번호 -> 가로 길이
import sys

w, h = map(int, sys.stdin.readline().split())
row = [0, w]
column = [0, h]

for i in range(int(input())):
    direction, coor = map(int, input().split())
    if (direction == 0):
        column.append(coor)
    else:
        row.append(coor)

row.sort()
column.sort()

r_length = []
c_length = []

for i in range(len(row)-1):
    r_length.append(row[i+1] - row[i])
for i in range(len(column) -1):
    c_length.append(column[i+1] - column[i])

print(max(c_length) * max(r_length))



