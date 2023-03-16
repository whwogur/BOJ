import sys
# 백준_9020
# 골드바흐의 추측
# 수를 반으로 나누고 하나는 1씩 줄여나가면서, 하나는 1씩 늘려나가면서 둘다 소수인지 확인
def isPrime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

n = int(input())

for i in range(n):
    num = int(input())
    a, b = num/2 , num/2

    while(b > 0):
        if (isPrime(a) and isPrime(b)):
            print(int(b), int(a))
            break
        a += 1
        b -= 1
