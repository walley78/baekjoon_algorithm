def solution(number, k):
    # 빈 배열 만들어
    stack = []
    for num in number:
        # 스택 안에 값이 있고
        # 스택의 맨 마지막 원소가 지금 num보다 작으면 맨 마지막 원소 퇴출시켜
        # 그리고 k가 0보다 클 동안만 실행 
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    # 혹시 stack의 크기가 써야하는 숫자자리를 벗어났을 경우를 대비해 딱 맞게 자른다
    answer = ''.join(stack[:len(stack)-k])
    return answer