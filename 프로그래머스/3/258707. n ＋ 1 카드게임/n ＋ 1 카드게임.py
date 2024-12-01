from collections import deque

def solution(coin, cards):
    N = len(cards)
    first_cards = set(cards[:N//3])
    rest_cards = deque(cards[N//3:])
    possible = set()

    def update_possible():
        # 새로 뽑은 카드 두장을 일단 possible 에 저장 (쓸지 안쓸지 모름)
        if rest_cards:
            possible.add(rest_cards.popleft())
            possible.add(rest_cards.popleft())

    # source에서 숫자 하나를 고르고, 그 숫자에 맞는 쌍을 target에서 찾는다
    # 찾는 데 성공했다면 True를 반환하고, 실패했다면 False를 반환
    def remove_pair(source: set, target: set) -> bool:
        nonlocal coin, round
        for x in list(source):
            if N+1-x in target:
                source.remove(x)
                target.remove(N+1-x)
                return True
        return False

    # 1라운드에서부터 시작
    round = 1
    while rest_cards:
        # 새로 카드 두장 뽑아
        update_possible()
        # 가지고 있는 카드들로만 n+1 만들수있으면 다음 라운드로 가
        if remove_pair(first_cards, first_cards):
            round += 1
        # 코인이 1개 이상 있고 가지고 있는 카드 + 뽑아서 저장해둔 카드로 n+1 만들수 있으면
        # 코인 하나 소모하고 다음 라운드
        elif coin >= 1 and remove_pair(first_cards, possible):
            coin -= 1
            round += 1
        # 코인이 2개 이상에 뽑아서 저장해둔 카드들로만 n+1 만들 수 있으면
        # 코인 두 개 소모하고 다음 라운드
        elif coin >= 2 and remove_pair(possible, possible):
            coin -= 2
            round += 1
        else:
            break

    return round