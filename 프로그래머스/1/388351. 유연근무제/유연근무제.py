def solution(schedules, timelogs, startday):
    
    def earlywakey(dtime, timelog, startday):
        # 출근 희망시간이 50분 이상이면 '시'에 1을 더하고 '분'-50을 할것
        if dtime%100 >= 50:
            temphr = dtime//100 + 1
            tempmin = dtime%100 - 50
            dtime = temphr*100+tempmin
        # 출근 희망시간이 50분 미만이면 그냥 10 더한숫자보다 출근숫자가 작으면됨
        else:
            dtime += 10
        wakecount = 0
        for wakeuptime in timelog:
            # 주말이 아니고
            if startday not in {6, 7}:
                if wakeuptime <= dtime:
                    wakecount += 1
            if startday < 7:
                startday += 1
            elif startday >= 7:
                startday = 1
        
        if wakecount == 5:
            return True
        else:
            return False
        
    prize = 0
    for person in range(len(schedules)):
        determined_time = schedules[person]
        timelog = timelogs[person]
        if earlywakey(determined_time, timelog, startday):
            prize += 1
        
    return prize