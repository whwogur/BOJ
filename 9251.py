# 9251 LCS
# 일치할 경우 dp[i][j] = dp[i-1][j-1] + 1
# 불일치 할 경우 dp[i][j] = Max(dp[i-1][j], dp[i][j-1])
import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = list(input().rstrip())

m = len(str1)
n = len(str2)

def LCS_dp(str1, str2, m, n):
    table = []

    # m행 n열 0으로 초기화된 table 생성
    for i in range(m+1):
        line = []
        for j in range(n+1):
            line.append(0)
        table.append(line)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]: # 공통부분에 포함되기 때문에 LCS에도 추가
                table[i][j] = table[i-1][j-1] + 1
            else: # LSC에 포함되지 않으므로, 이전까지의 LCS와 동일하게 유지
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return table

result = LCS_dp(str1, str2, m, n)
print(result[m][n])