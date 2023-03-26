# 9252 LCS 2
import sys
input = sys.stdin.readline

word1 = [''] + list(input().strip())
word2 = [''] + list(input().strip())
l_1, l_2 = len(word1), len(word2)
dp = [[''] * l_2 for i in range(l_1)]

for i in range(l_1):
    for j in range(l_2):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i - 1][j - 1] + word1[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[l_1 - 1][l_2 - 1]))
print(dp[l_1 - 1][l_2 - 1])