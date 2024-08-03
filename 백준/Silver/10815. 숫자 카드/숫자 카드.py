import sys
input = sys.stdin.readline

N = int(input())
sangun_cards = set(map(int, input().split()))
M = int(input())
find_cards = list(map(int, input().split()))

for num in find_cards:
    if num in sangun_cards:
        print(1)
    else:
        print(0)


# 상근이가 가지고 있는 숫자 카드인지 아닌지 구해야
# 갖고 있으면 1, 아니면 0
