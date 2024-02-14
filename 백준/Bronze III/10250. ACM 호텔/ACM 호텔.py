T = int(input())

for tc in range(1, T + 1):
    H, W, N = map(int, input().split())  # 각각 호텔의 층수 ,각 층의 방수, 몇 번째 손님

    # 이런건 규칙 안 찾으면 답이 없네

    # 손님이 머무를 방 층수는 N % H 층이다.
    floor = N % H
    # 손님이 머무를 방 호수는 N // H + 1호이다.
    room = N // H + 1
    # 나누어 떨어질 경우 손님이 머물 방은 H 층이다
    if N % H == 0:
        floor = H
        room = N // H
     
    # 402호, 1204호, 이러니까 층에 100 곱한것에 방 호수 더해주기
    print(floor*100 + room)
