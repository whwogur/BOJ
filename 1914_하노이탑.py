# 백준 1914
# 하노이 탑
# EX) 3개 ( 매개변수 )
# 3 , 1 , 3
#           2 , 1 , 2
#                     1 , 1 , 3
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n - 1, start, 6-start-end)
    print(n,start, end)
    hanoi(n - 1, 6-start-end, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)
