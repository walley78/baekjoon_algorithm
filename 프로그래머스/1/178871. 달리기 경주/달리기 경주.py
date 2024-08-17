def solution(players, callings):
    playerdic = dict()
    for idx, value in enumerate(players):
        playerdic[value] = idx
    for player in callings:
        before_rank = playerdic[player]
        playerdic[player] -= 1
        now_rank = playerdic[player]
        playerdic[players[now_rank]] += 1
        players[before_rank], players[now_rank] = players[now_rank], players[before_rank]
    return players