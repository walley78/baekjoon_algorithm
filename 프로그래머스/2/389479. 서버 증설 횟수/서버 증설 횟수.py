def solution(players, m, k):
    answer = 0
    # players의 길이 24
    # players[i]는 i시~i+1시 사이의 게임 이용자 수를 나타냄
    expand = [0]*24
    add = 0
    # 증설하면 (i+k)-1 까지 증설된수 카운트
    for i in range(24):
        # print(f"지금은 {i}시간입니다.")
        # print(f"players[{i}]는 {players[i]}입니다")
        # print(f"expand[{i}]는 {expand[i]}입니다")
        # print(f"players[{i}]//m은 {players[i]//m}입니다")
        # 플레이어가 m명 이상이고 expand[i]에 증설서버가 모자라면 증설해야해
        if players[i] >= m and expand[i] < players[i]//m:
            # print(f"플레이어가 m명 이상이고 증설한 서버가 모자랍니다")
            temp = expand[i]
            # print(f"temp는 {temp}입니다")
            # expand[i] += players[i]//m
            # i부터 i+k시간(아니면 24시간)까지 players[i]//(m-expand[j])
            for j in range(i, min(24, i+k)):
                expand[j] += (players[i]//m-temp)
            add += players[i]//m-temp

            # print(expand)
            # print(add)
            # print("--------안쪽 for문 끝------------")
        # print(expand)
        # print("------바깥 for문 끝--------")
    return add