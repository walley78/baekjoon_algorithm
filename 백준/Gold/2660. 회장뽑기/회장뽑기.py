import sys
from collections import deque

input = sys.stdin.readline


# 첫째 줄은 회원의 수
membersNum = int(input())

# 멤버는 1부터 시작함
members = [[] for _ in range(membersNum+1)]

flag = True

while flag:
    mem1, mem2 = map(int, input().split())
    if mem1 == -1:
        flag = False
        break
    members[mem1].append(mem2)
    members[mem2].append(mem1)

# print(members)

captain = []

def score(member, start):
    count = 0
    # 이 멤버 점수
    memberscore = [0]*(membersNum+1)
    # 일단 이 멤버랑 1점인 친구들부터 시작
    stack = members[member]
    temp = []
    # 첫 회원부터 돌아 (끝 회원까지)
    while start != membersNum+1:
        count += 1
        # 스택의 친구들 하나씩 꺼내면서 자기자신과 같지 않으면 temp에 추가
        for next in stack:
            if next != member:
                if memberscore[next] == 0:
                    memberscore[next] = count
                temp.extend(members[next])
        # 멤버점수 1점 추가
        start += 1
        # 스택 아까 temp에 추가한걸로 바꿔치기
        stack = set(temp)
        temp = []
    # print(memberscore)
    return max(memberscore)

for mem in range(1, membersNum+1):
    memscore = score(mem, 1)
    if captain:
        if captain[0][1] < memscore:
            continue
        elif captain[0][1] == memscore:
            captain.append([mem, memscore])
        elif captain[0][1] > memscore:
            captain = [[mem, memscore]]
    else:
        captain = [[mem, memscore]]
    captain.sort(key=lambda x: x[1])



print(captain[0][1], len(captain))

ans = []
for candidates in captain:
    ans.append(candidates[0])

print(*ans)