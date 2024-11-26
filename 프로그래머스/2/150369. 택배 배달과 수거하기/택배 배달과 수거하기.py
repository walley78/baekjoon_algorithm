def solution(cap, n, deliveries, pickups):
    # 총 이동 거리 초기화
    total_distance = 0

    # 배달 및 수거할 택배가 없는 끝 부분 제거
    while n > 0 and deliveries[n - 1] == 0 and pickups[n - 1] == 0:
        n -= 1

    # 배달 및 수거를 추적할 스택 생성
    delivery_stack = []
    pickup_stack = []

    # 0이 아닌 값들로 스택 준비
    for i in range(n):
        if deliveries[i] > 0:
            delivery_stack.append((i + 1, deliveries[i]))
        if pickups[i] > 0:
            pickup_stack.append((i + 1, pickups[i]))

    # 배달 및 수거 처리
    while delivery_stack or pickup_stack:
        # 이번 트립에서 가장 먼 집 거리 초기화
        max_distance = 0

        # 이번 트립의 배달 적재량 추적
        delivery_load = 0
        delivery_trip = []

        # 배달 처리
        while delivery_stack and delivery_load < cap:
            dist, amount = delivery_stack.pop()
            # 가장 먼 집 거리 업데이트
            max_distance = max(max_distance, dist)

            # 실을 수 있는 만큼 배달
            to_deliver = min(cap - delivery_load, amount)
            delivery_load += to_deliver

            # 남은 택배가 있다면 다시 스택에 추가
            if to_deliver < amount:
                delivery_stack.append((dist, amount - to_deliver))
                break

        # 이번 트립의 수거 적재량 추적
        pickup_load = 0
        pickup_trip = []

        # 수거 처리
        while pickup_stack and pickup_load < cap:
            dist, amount = pickup_stack.pop()
            # 가장 먼 집 거리 업데이트
            max_distance = max(max_distance, dist)

            # 실을 수 있는 만큼 수거
            to_pickup = min(cap - pickup_load, amount)
            pickup_load += to_pickup

            # 남은 빈 택배상자가 있다면 다시 스택에 추가
            if to_pickup < amount:
                pickup_stack.append((dist, amount - to_pickup))
                break

        # 왕복 거리 추가
        total_distance += max_distance * 2

    return total_distance