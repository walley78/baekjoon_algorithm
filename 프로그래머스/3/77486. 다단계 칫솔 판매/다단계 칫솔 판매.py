def solution(enroll, referral, seller, amount):
    # 미리 딕셔너리에 매칭되는 인덱스와 이름 저장해둠
    index_map = {name: idx for idx, name in enumerate(enroll)}
    parent_map = {child: parent if parent != '-' else 'center' for child, parent in zip(enroll, referral)}
    profits = [0] * len(enroll)

    # 수익 계산
    for sale, num in zip(seller, amount):
        current = sale
        current_profit = num * 100

        while current != 'center' and current_profit > 0:
            # print(f"current: {current} | current profit: {current_profit}")
            parent = parent_map[current]
            parent_idx = index_map[parent] if parent != 'center' else None
            commission = int(current_profit * 0.1)

            # 1원 미만이면 부모에게 안 나눠줌
            if commission < 1:
                profits[index_map[current]] += current_profit
                break

            # 1원 이상이면 나눠줌
            profits[index_map[current]] += (current_profit - commission)
            # print(profits)
            current_profit = commission
            current = parent

    return profits