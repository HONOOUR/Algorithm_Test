# DP[N]: N번째를/까지 선택했을 때 최적 
# 2
# 5
# 50 10 100 20 40
# 30 50 70 10 60
# 7
# 10 30 10 50 100 20 40
# 20 40 30 50 60 20 80


DP = []
for _ in range(2):
    DP.append(list(map(int, input().split())))
n = len(DP[0])
for i in range(2, ):
    DP[0][i] += max(DP[1][i-2], DP[1][i-1])
    DP[1][i] += max(DP[0][i-2], DP[0][i-1])
max(DP[0][n-1], DP[1][n-1])