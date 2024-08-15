def solution(keymap, targets):
    answer = []
    keymapdic = dict()
    for key in keymap:
        temp = list(key)
        for i in range(len(temp)):
            if keymapdic.get(temp[i]):
                keymapdic[temp[i]] = min(i+1, keymapdic[temp[i]])
            else:
                keymapdic[temp[i]] = i+1
    # print(keymapdic)
    cnt = 0
    for target in targets:
        for i in range(len(target)):
            if keymapdic.get(target[i]):
                cnt += keymapdic[target[i]]
            else:
                answer.append(-1)
                cnt = 0
                break
        else:
            answer.append(cnt)
            cnt = 0
    return answer
