def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return f'{h:02d}:{m:02d}:{s:02d}'

def solution(play_time, adv_time, logs):
    play_seconds = time_to_seconds(play_time)
    adv_seconds = time_to_seconds(adv_time)
    total_time = [0] * (play_seconds + 2)

    for log in logs:
        start_str, end_str = log.split('-')
        start = time_to_seconds(start_str)
        end = time_to_seconds(end_str)
        total_time[start] += 1
        total_time[end] -= 1

    # 누적 시청자 수 계산
    for i in range(1, play_seconds + 1):
        total_time[i] += total_time[i - 1]

    # 누적 재생 시간 계산
    for i in range(1, play_seconds + 1):
        total_time[i] += total_time[i - 1]

    max_time = total_time[adv_seconds - 1]
    max_start = 0

    for start in range(1, play_seconds - adv_seconds + 1):
        end = start + adv_seconds - 1
        current_time = total_time[end] - total_time[start - 1]
        if current_time > max_time:
            max_time = current_time
            max_start = start

    return seconds_to_time(max_start)