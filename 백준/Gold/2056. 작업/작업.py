from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

# 두번째 줄부터 N+1번째 줄까지 N개의 줄이 주어짐
# 2번째 줄은 1번 작업, 3번째 줄은 2번 작업... N+1번째 줄은 N번 작업을 각각 나타냄
# 각 줄의 처음엔 해당 작업에 걸리는 시간, 그 작업에 대해 선행 관계에 있는 작업들의 개수
# 그리고 선행 관계에 있는 작업들의 번호

works = [0]*(N+1)
workdict = {idx:[] for idx in range(1, N+1)}

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    # i번작업하는데 걸리는 시간
    works[i] = temp[0]
    # 딕셔너리에 선행되어야하는 작업 저장
    workdict[i] = temp[2:]

def calctime(idx, time):
    # 선행되어야하는 작업리스트 확인
    stack = deque(workdict[idx])
    max_time = 0
    # 선행작업이 존재하는 동안 선행작업 뽑아
    if stack:
        while stack:
            previdx = stack.popleft()
            # 작업시간은 선행작업시간 + 현재작업시간
            newtime = time + works[previdx]
            max_time = max(max_time, newtime)
    return max(max_time, time)

for i in range(1, N+1):
    addedtime = calctime(i, works[i])
    works[i] = addedtime

print(max(works))
# print(works[-1])