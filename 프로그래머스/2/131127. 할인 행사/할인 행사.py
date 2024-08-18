from copy import deepcopy

def solution(want, number, discount):
    wantdic = dict()
    for i in range(len(want)):
        wantdic[want[i]] = number[i]

    def tendays(dic, discount):
        tempdic = deepcopy(dic)
        for i in range(10):
            if tempdic.get(discount[i]) and tempdic[discount[i]] > 0:
                tempdic[discount[i]] -= 1
            else:
                return False
        else:
            return True

    daycount = 0
    for i in range(len(discount)-10+1):
        if tendays(wantdic, discount[i:i+10]):
            daycount += 1

    return daycount