import sys

input = sys.stdin.readline

def max_stair_score(N, stair):
    # 다음 계단 밟거나, 다다음 계단 밟거나
    # 마지막 계단은 무조건 밟아야함
    # 계단이 한개뿐이면 그거 밟으면 끝
    if N == 1:
        return stair[0]
    # 계단이 두 개뿐이면 둘 다 밟으면 됨
    elif N == 2:
        return stair[0] + stair[1]
    else:
        # dp 리스트 만들자
        dp = [0] * N
        # 0개면 stair 1개
        dp[0] = stair[0]
        # 2개면 첫번째 + 두번째 stair
        dp[1] = stair[0] + stair[1]
        # 3번째는 1번째 (0번째) 계단 + 3번째합 (2) 계단의 합 아니면
        # 2번째 (1) 계단 + 3번째 (2) 계단의 합 중 더 큰 쪽으로
        dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

        # 4번째부터는
        # 건너뛰어서 4번째로 바로 오는지
        # 저저번에 건너뛰고 3번째 밟고 4번째로 오는지
        # 2 4 던지
        # 건너뛰어서 4번째로 바로 오는 경우 그 이전에 연속으로 밟았는지 또 건너뛰었는지 알 수 없기 때문에
        # 그 이전 값은 적지 않음 
        # 1 3 4 던지 
        for i in range(3, N):
            # i번째 이전은 dp에 값이 있지만 i번째 dp는 이전 stair 값들 (dp 에 저장된)
            # 더하기 stair[i]를 해줘야함
            dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

        return dp[N-1]


# 첫째 줄에 계단의 개수
# 둘째 줄부터 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다

N = int(input().strip())

stair = [int(input().strip()) for _ in range(N)]

result = max_stair_score(N, stair)

print(result)