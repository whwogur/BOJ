# 1439 뒤집기
string = input()
cnt = 0
for i in range(len(string)-1):
    if string[i] != string[i + 1]:
        cnt += 1
print((cnt + 1) // 2)