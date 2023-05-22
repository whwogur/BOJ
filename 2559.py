# 2559 수열
_, k = map(int, input().split())
temp = list(map(int, input().split()))
seg = sum(temp[:k])
answer = [seg]
for i in range(0, len(temp)-k):
    seg = seg - temp[i] + temp[i+k]
    answer.append(seg)
print(max(answer))