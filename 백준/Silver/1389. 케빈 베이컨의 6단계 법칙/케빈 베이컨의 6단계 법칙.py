import sys
from collections import deque

input = sys.stdin.readline


# 첫째 줄에 유저의 수와 친구 관계의 수
N, M = map(int, input().split())

# 사람의 번호는 1부터 N까지
friendship = [[] for _ in range(N+1)]

# M개의 줄에 친구 관계 A, B
for _ in range(M):
    # A, B가 친구면 B, A도 친구
    A, B = map(int, input().split())
    friendship[A].append(B)
    friendship[B].append(A)

# print(friendship)

# 현재 num, 그리고 1부터 돌아
def friendshiplevel(num, i):
    level = [0] * (N + 1)
    lev = 1
    stack = set(friendship[num])
    while i != N+1:
        tempstack = []
        for next in stack:
            if level[next] == 0:
                level[next] = lev
            tempstack.extend(friendship[next])
        stack = set(tempstack) - {num}
        i += 1
        lev += 1

    return sum(level)

# print(friendshiplevel(1, 1))

sumkevin = [0]*(N+1)

for i in range(1, N+1):
    kevin = friendshiplevel(i, 1)
    sumkevin[i] = kevin

# print(sumkevin)
minidx = sumkevin.index(min(sumkevin[1:]))

print(minidx)