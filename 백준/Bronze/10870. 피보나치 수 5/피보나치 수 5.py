import sys
input = sys.stdin.readline

N = int(input())

# n은 0 <= n < = 20
# n이 0일 경우의 수도 고려해야함!!!
dp = [0] * (N+1)

if N == 0:
    print(0)
else:  
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
        # print(dp[i])
    
    print(dp[N])