# 1264 모음의 개수
import sys
dic = {'a','e','i','o','u','A','E','I','O','U'}
while True:
    string = list(input().rstrip())
    if string[0] == '#': break
    else:
        cnt = 0
        for i in string:
            if i in dic:
                cnt += 1
        print(cnt)