def solution(s):
    result = []
    # 다음번에 대문자할지말지 결정
    capitalize_next = True

    for char in s:
        # char가 알파벳이고 대문자로 만들차레면
        if char.isalpha() and capitalize_next:
            result.append(char.upper())
            capitalize_next = False
        else:
            # 알파벳이 아니면
            # 공백이면 result append하고
            if char == ' ':
                result.append(char)
                capitalize_next = True
            # 숫자면 그대로 result에 append
            elif not char.isalpha():
                result.append(char)
                capitalize_next = False
            elif char.isalpha() and not capitalize_next:
                result.append(char.lower())
                capitalize_next = False

    answer = ''.join(result)
    return answer
