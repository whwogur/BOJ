# 1541 잃어버린 괄호
import sys
input = sys.stdin.readline

string = input().rstrip().split('-') # 55-50+40
nums = []

for i in string: # ['55','50+40']
    cnt = 0
    s = i.split('+') # ['55'],['50','40']
    for j in s:
        cnt += int(j)
    nums.append(cnt) # ['55', '90']
n = nums[0] # 55
for i in range(1, len(nums)):
    n -= nums[i]
print(n)