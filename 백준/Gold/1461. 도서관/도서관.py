import sys

input = sys.stdin.readline


# 세준이와 사람들이 마구 놓은 책들이 전부 0에 있음
# 책을 모두 제자리에 놔둘 떄 드는 최소 걸음 수
# 한 걸음에 좌표 1칸
# 제자리에 놔둔 뒤 0으로 돌아올 필요 없음
# 한번에 최대 M권의 책 들 수 있음
# N과 M은 50보다 작거나 같은 자연수

# 책의 개수 N과 세준이가 한번에 들 수 있는 책 M
booknum, power = map(int, input().split())

original_places = list(map(int, input().split()))

positive_places = []
negative_places = []

original_places.sort()

for place in original_places:
    if place > 0:
        positive_places.append(place)
    else:
        negative_places.append(abs(place))

negative_places.sort()

# 제일 먼 쪽을 마지막에 해야돼 (다시 0으로 안 돌아와도 되니까 걸음수 최소화 가능)
# 제일 먼 쪽에서부터 M개는 제일 먼 곳 갈때 해치워
# 제일 먼 쪽에서부터 M개 이전부터 M개씩 왔다갔다

# print(original_places)
# print(positive_places)
# print(negative_places)

walk = 0

# 마지막에 갈 곳을 정하자
# positive place[-1] 이 더 크면 걔를 마지막, 아니면 negative place[-1]을 마지막으로

positive_N = len(positive_places)
negative_N = len(negative_places)

def calcwalkcount(endidx, power, placelist):
    walkcount = 0
    flag = True
    while flag:
        if endidx == 0:
            walkcount += placelist[endidx]*2
            # print("endidx is: ", endidx, "placelist[endidx] is: ", placelist[endidx])
            # print("walkcount is: ", walkcount)
            break
        else:
            walkcount += placelist[endidx]*2
            # print("endidx is: ", endidx, "placelist[endidx] is: ", placelist[endidx])
            # print("walkcount is: ", walkcount)
            endidx = endidx-power
            if endidx < 0:
                # print("covered everything")
                break
    return walkcount

if positive_places and negative_places:
    if positive_places[-1] >= negative_places[-1]:
        walk += positive_places[positive_N-1]
        # print("양수리스트[-1]이 더 커서 거기를 왕복 안하기로 함: ", walk)
        # if positive_N-power-1 < 0:
            # print("covered everything")
        if positive_N-power-1 >= 0:
            poscount = calcwalkcount(positive_N-power-1, power, positive_places)
            walk += poscount
        negcount = calcwalkcount(negative_N-1, power, negative_places)
        walk += negcount
    elif negative_places[-1] > positive_places[-1]:
        walk += negative_places[negative_N-1]
        # print("음수리스트[-1]이 더 커서 거기를 왕복 안하기로 함: ", walk)
        # if negative_N-power-1 < 0:
        #     print("covered everything")
        if negative_N-power-1 >= 0:
            negcount = calcwalkcount(negative_N-power-1, power, negative_places)
            walk += negcount
        poscount = calcwalkcount(positive_N-1, power, positive_places)
        walk += poscount
elif positive_places:
    walk += positive_places[positive_N - 1]
    # print("양수리스트밖에 존재 안함: ", walk)
    # if positive_N - power - 1 < 0:
        # print("covered everything")
    if positive_N-power-1 >= 0:
        poscount = calcwalkcount(positive_N - power - 1, power, positive_places)
        walk += poscount
elif negative_places:
    walk += negative_places[negative_N - 1]
    # print("음수리스트밖에 존재 안함 ", walk)
    # if negative_N - power - 1 < 0:
        # print("covered everything")
    if negative_N-power-1 >= 0:
        negcount = calcwalkcount(negative_N - power - 1, power, negative_places)
        walk += negcount

print(walk)
