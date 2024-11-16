import sys

input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input().split()))
S = int(input())

for start in range(N):
    max_pos = start
    # 바꿀 수 있는 거리 안에서 최대인 수를 찾는다
    for i in range(start + 1, min(N, start + S + 1)):
        if numlist[i] > numlist[max_pos]:
            max_pos = i

    # 최대인 수를 왼쪽 옆에 있는 수랑 바꿔치기해서 계속해서 버블해서 올라옴 (S번)
    while max_pos > start and S > 0:
        numlist[max_pos], numlist[max_pos - 1] = numlist[max_pos - 1], numlist[max_pos]
        max_pos -= 1
        S -= 1

print(*numlist)