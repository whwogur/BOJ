# 9252 LCS 2
import sys
input = sys.stdin.readline

word1 = [''] + list(input().strip())
word2 = [''] + list(input().strip())
len_1, len_2 = len(word1), len(word2)
dp = [[''] * len_2 for _ in range(len_1)]

for i in range(len_1):
    for j in range(len_2):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i - 1][j - 1] + word1[i]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[len_1 - 1][len_2 - 1]))
print(dp[len_1 - 1][len_2 - 1])