def solution(cards1, cards2, goal):
    answer = ''
    idx = 0
    idx1 = 0
    idx2 = 0
    # 각 배열 앞에서부터 무조건써야함
    while idx < len(goal):
        if idx1 < len(cards1) and goal[idx] == cards1[idx1]:
            answer += goal[idx]
            idx += 1
            idx1 += 1
        elif idx2 < len(cards2) and goal[idx] == cards2[idx2]:
            answer += goal[idx]
            idx += 1
            idx2 += 1
        else:
            answer = 'No'
            return answer
    # print(answer)
    # print(''.join(goal))
    if answer == ''.join(goal):
        answer = 'Yes'

    return answer