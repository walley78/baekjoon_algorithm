import sys

input = sys.stdin.readline

def fibonacci(num, memo):
    # 이미 해당 숫자의 0과 1 개 메모해뒀으면 그거 return 하면 돼
    if num in memo:
        return memo[num]
    # num이 0이면 0이 1개
    if num == 0:
        # print(0)
        # zero가 1개, 1은 0개 - 기록해두기
        memo[num] = (1, 0)
        # return 0
        return memo[num]
    # num 1이면 1이 1개지
    elif num == 1:
        # print(1)
        # zero 0개, 1이 1개 - 기록해두기
        memo[num] = (0, 1)
        return memo[num]
    else:
        # num이 0도 1도 아니면 0과 1이 될때까지 쪼개야지
        z1, o1 = fibonacci(num-1, memo)
        z2, o2 = fibonacci(num-2, memo)
        # 지금 이 num의 1과 0 개수들은 각각 1 빼고 2 뺀 것들의 합
        memo[num] = (z1+z2, o1+o2)
        return memo[num]

# fibonacci(3)

N = int(input())

# 메모할 것 준비
# 해당 num의 (0 개수, 1 개수)
memo = {}

for _ in range(N):
    num = int(input())
    cnt_z, cnt_o = fibonacci(num, memo)
    print(f"{cnt_z} {cnt_o}")