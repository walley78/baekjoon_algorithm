def solution(n):
    answer = []
    
    def hanoi(source, temp, target, n):
        # n=1 (마지막원반)이면 최종타겟기둥에 가져다놔
        if n == 1:
            answer.append([source, target])
        else:
            # n-1개의 원반까지는 임시에다 옮겨놓음
            hanoi(source, target, temp, n-1)
            # 마지막 남은 원반 (큰놈) 이동시켜
            hanoi(source, temp, target, 1)
            # 이제 임시에다 옮겨놓은 n-1개의 원반들 타겟으로 이동시켜
            hanoi(temp, source, target, n-1)
    hanoi(1, 2, 3, n)
    
    return answer