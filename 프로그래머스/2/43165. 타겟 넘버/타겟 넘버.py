def solution(numbers, target):
    count = 0
    # 빼고
    # 더해보고
    def gettarget(number, idx):
        nonlocal count
        if idx == len(numbers):
            if number == target:
                count += 1
            return

        gettarget(number+numbers[idx], idx+1)
        gettarget(number-numbers[idx], idx+1)

    gettarget(0, 0)

    return count