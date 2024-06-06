import sys

input = sys.stdin.readline

# x가 3으로 나누어떨어지면 3으로 나눈다
# x가 2로 나누어떨어지면 2로 나눈다
# 1을 뺀다

def min_ways_to_one(N):
    # N 사이즈의 dp 만들기 (인덱스 2부터 시작하니까 N+1 사이즈)
    # 각 인덱스의 숫자를 1로 만드는데 필요한 count
    dp = [0] * (N+1)

    # 2부터 시작함 (1로 만드는게 목적인데 굳이 dp[1]을 할필요는 없으니까
    # 현재 값에 1을 더해주는 이유는 1을뺐든 2, 3을 곱했든 어떤 동작을 했으니까 그걸 포함시켜주는것 
    for i in range(2, N+1):
        # 1 먼저 빼보기  
        dp[i] = dp[i-1] + 1

        # i가 2로 나누어떨어지면 2로 나눴을 때의 count랑 현재 값이랑 비교
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
            
        # 3으로 나눠떨어졌을때 3으로 나눴을때의 count랑 현재 값이랑 비교 
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    return dp[N]


N = int(input())

print(min_ways_to_one(N))

