import sys
input = sys.stdin.readline

nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, num = map(int, input().split())
answer = ''

while n > 0:
    answer += str(nums[n % num])
    n //= num

print(answer[::-1])