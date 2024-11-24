import sys

n, d = map(int, sys.stdin.readline().split())

dp = [i for i in range(d+1)]

shortcuts = []

for _ in range(n):
    start, end, dist = map(int, sys.stdin.readline().split())
    if end - start > dist and not end > d:
        shortcuts.append((start, end, dist))
shortcuts.sort()

for start, end, dist in shortcuts:
    # 고속도로 길이만큼 돌려
    for i in range(1, d+1):
        # 지름길 도착지랑 i랑 똑같아지면 고속도로 i위치까지 가는데
        # 걸리는 거리 중에서 최소인 쪽을 골라
        if end == i:
            dp[i] = min(dp[i], dp[start]+dist)
        # 지름길 도착지랑 i랑 안 다르면
        # 현재 고속도로 i번째 위치 = i-1번째에서 +1한것과 현재 위치의 값 중 최솟값인 걸로
        else:
            dp[i] = min(dp[i], dp[i-1]+1)

print(dp[d])