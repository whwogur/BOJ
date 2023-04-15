# 1193 분수찾기
n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line % 2 == 0:
    numer = line - diff
    denom = diff + 1
else:
    numer = diff + 1
    denom = line - diff

print("%d/%d"%(numer,denom))