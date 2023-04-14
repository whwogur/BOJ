# 4948 베르트랑 공준
def prime(n): # 에라토테네스의 체
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

nums = list(range(2,246912)) # 1 <= n <= 123,456
memo = []

for i in nums:
    if prime(i):
        memo.append(i)

n = int(input())

while True:
    cnt = 0
    if n == 0 :
            break
    for i in memo:
        if n < i <=2*n:
            cnt+=1
    print(cnt)
    n = int(input())