def solution(progresses, speeds):
    days = []
    answer = []
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        if left % speeds[i] != 0:
            left_day = left // speeds[i] + 1
        else:
            left_day = left // speeds[i]
        days.append(left_day)
    together = 1
    print(days)
    temp = days.pop(0)
    while days:
        if temp >= days[0]:
            together += 1
            if len(days) == 1:
                answer.append(together)
                days.pop(0)
            else:
                days.pop(0)
                continue
        else:
            answer.append(together)
            together = 1
            if len(days) == 1:
                answer.append(together)
                days.pop(0)
            else:
                temp = days.pop(0)

    return answer