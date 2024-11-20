import sys
input = sys.stdin.readline

N = int(input().strip())

weights = list(map(int, input().strip().split()))
weights.sort()
# print(weights)

# 저울추로 잴 수 없는 가장 작은 숫자 : 일단은 1
smallest_unmeasurable = 1

for weight in weights:
    # print("현재 weight: ", weight)
    # 현재 무게가 가장 작은 숫자보다 크면 가장 작은 숫자를 잴 수 없다는 뜻 : break
    if weight > smallest_unmeasurable:
        break
    # 아니면 잴 수 있음
    smallest_unmeasurable += weight
    # print("업데이트된 가장 작은 숫자", smallest_unmeasurable)

print(smallest_unmeasurable)