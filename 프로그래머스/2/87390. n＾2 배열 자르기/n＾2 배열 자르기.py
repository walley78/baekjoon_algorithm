def solution(n, left, right):
    answer = []
    # 규칙
    # 1 (0, 0) 2 (0, 1) 3 (0, 2) 2 (1, 2) 2 (1, 2) 3 (1, 2)
    # 0        1        2        3        4        5
    for i in range(left, right+1):
        a = i // n
        b = i % n
        if a < b:
            answer.append(b+1)
        else:
            answer.append(a+1)
    
    return answer