from heapq import heappop, heappush

import sys

input = sys.stdin.readline

# 연산의 개수
N = int(input())

# 다음 N개의 줄에 연산에 대한 정보를 나타내는 정보 x
# x가 자연수라면 배열에 x 추가
# x가 0이라면 배열에서 가장 작은 값 출력
# x가 0인데 배열이 비었으면 그냥 0 출력

arr = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if arr:
            print(heappop(arr))
        else:
            print(0)
    else:
        heappush(arr, x)