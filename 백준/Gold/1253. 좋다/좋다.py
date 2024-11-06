import sys

input = sys.stdin.readline

N = int(input())

# N개의 수 중에서 어떤 수가 다른 수 두개의 합으로 나타낼 수 있으면 좋다
# 좋은 수의 개수는?
# 수의 위치가 다르면 값이 같아도 다른 수이다 (중복 수 존재 가능)
numlist = list(map(int, input().split()))
numset = set(numlist)
numcount = set()
numdict = dict()

for i in range(len(numlist)):
    if numdict.get(numlist[i]):
        numdict[numlist[i]].add(i)
    else:
        numdict[numlist[i]] = {i}


def findnum():
    good_count = 0
    for i in range(len(numlist)):
        for j in range(i+1, len(numlist)):
            numsum = numlist[i]+numlist[j]
            if numsum in numset and numsum not in numcount:
                if numlist[i] == numsum:
                    if not numdict[numlist[i]] - {i}:
                        continue
                if numlist[j] == numsum:
                    if not numdict[numlist[j]] - {j}:
                        continue
                if numlist[i] == numlist[j] == numsum:
                    if not numdict[numlist[i]] - {i, j}:
                        continue
                numcount.add(numsum)
                good_count += numlist.count(numsum)
                # print("good_count is: ", good_count)

    return good_count


ans = findnum()

print(ans)