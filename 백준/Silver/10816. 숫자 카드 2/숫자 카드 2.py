import sys
input = sys.stdin.readline

# 상근이가 몇개가지고있는 숫자카드인지?

N = int(input())
sangun_cards = list(map(int, input().split()))
M = int(input())
how_many = list(map(int, input().split()))

sangun_dict = dict()

for card in sangun_cards:
    sangun_dict.setdefault(card, 0)
    sangun_dict[card] += 1

answer = []

for card in how_many:
    sangun_dict.setdefault(card, 0)
    answer.append(str(sangun_dict[card]))

print(' '.join(answer))