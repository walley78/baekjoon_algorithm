import sys

input = sys.stdin.readline

# 동전 N종류, 가치의 합 K
N, K = map(int, input().split())
cnt = 0

coins = []

for _ in range(N):
    coin = int(input())
    coins.append(coin)

for coin in range(N-1, -1, -1):
    # coin 값이 K와 정확히 같을 경우도 커버해야함...
    if K - coins[coin] >= 0:
        cnt += K//coins[coin]
        K %= coins[coin]
    else:
        continue

print(cnt)