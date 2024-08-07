import sys
from collections import deque

input = sys.stdin.readline

total_people = int(input())
total_people += 1
find, target = map(int, input().split())

number_of_relationship = int(input())

family_relation = [[] for _ in range(total_people)]

# print(family_relation)

for _ in range(number_of_relationship):
    p, c = map(int, input().split())
    family_relation[p].append(c)
    family_relation[c].append(p)

# print(family_relation)


def findchonsu(start, target):
    # 시작지점과 촌수
    queue = deque([(start, 0)])
    visited = [False] * (total_people)

    while queue:
        current, chonsu = queue.popleft()
        if not visited[current]:
            visited[current] = True
            if current == target:
                return chonsu
            for neighbors in family_relation[current]:
                queue.append((neighbors, chonsu+1))

    return -1


print(findchonsu(find, target))