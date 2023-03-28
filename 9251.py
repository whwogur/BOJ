# 9251 LCS
import sys
input = sys.stdin.readline
MAXLEN = 1001

string1 = '' + input().strip()
string2 = '' + input().strip()
dp = [[0] * len(string2) for _ in range(len(string1))]

for i in range(1, len(string1)):
    for j in range(1, len(string1)):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])