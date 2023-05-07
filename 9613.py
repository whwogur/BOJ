# 9613 GCD의 합
import sys
import math
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    nums = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            ans += math.gcd(nums[i], nums[j])
    print(ans)