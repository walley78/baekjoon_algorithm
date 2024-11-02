import sys
from collections import deque

input = sys.stdin.readline

def howtall(student):
    i = 1
    stack = deque(students[student])
    tempdict = dict()
    tempstack = []
    visited = [False]*(N+1)
    while stack:
        for next in stack:
            if not visited[next]:
                visited[next] = True
                countdict[next] += 1
                tempdict[next] = 0
                tempstack.extend(students[next])
        stack = tempstack
        tempstack = []

    # print("이 학생은: ", student, tempdict)
    # biggerThanMe = len(tempdict.keys())
    studentcount[student] = len(tempdict.keys())
    return

# 1: 5, 4, 6, 2
# 2:
# 3: 4, 6, 2
# 4: 6, 2
# 5: 4, 6, 2
# 6:

# 나보다 작은 사람 인원수 count를 한다고 치면
# 1부터 돌면 5:1 , 4:1, 6:1, 2:1 (나보다 큰 사람은 총 4명)
# 2는 아무것도 없어서 패스 (나보다 큰 사람 없음)
# 3은 4: 2, 6:2, 2:2 (나보다 큰 사람 3명)
# 4는 6:3, 2:3 (나보다 큰 사람 2명)
# 5는 4:3, 6:4, 2:4 (나보다 큰 사람 3명)
# 6은 아무것도 없어서 패스
# 그럼 1: 없음, 2:4, 3:없음, 4:3, 5:1, 6:4

# 나보다 큰 사람 인원수 count

# 학생들 수와 두 학생 키를 비교한 횟수
N, M = map(int, input().split())

# 해당 students index에 자기보다 더 큰 학생들이 보관됨
students = [[] for _ in range(N+1)]

countdict = dict()
for i in range(1, N+1):
    countdict[i] = 0

# M개의 줄에 두 학생의 키를 비교한 결과
for _ in range(M):
    a, b = map(int, input().split())
    students[a].append(b)

studentcount = [0]*(N+1)

for i in range(1, N+1):
    howtall(i)
    # studentcount[i] = biggerThanMe

count = 0

for i in range(1, N+1):
    if studentcount[i] + countdict[i] == N-1:
        count += 1

# print(studentcount)
# print(countdict)

print(count)