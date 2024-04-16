from collections import deque

wordlist = []
while True:
    yes = True
    sentence = str(input())
    if sentence == '.':
        break
    if (sentence.count('(') != sentence.count(')')) or (sentence.count('[') != sentence.count(']')):
        print('no')
        continue
    # wordlist.append(sentence)
    # sentence.replace(" ", "")
    # 문장에 공백 없애
    sentence = ''.join(sentence.split())
    # print(sentence)

    temp = list(sentence)
    # print(temp)
    stack = deque()
    for i in range(len(temp)):
        # 그냥 문자들이면 continue
        if temp[i] not in ['(', '[', ')', ']']:
            # temp.pop(i)
            continue
        # 여는 괄호면 (, [ 집어넣어
        elif temp[i] in ['(', '[']:
            stack.append(temp[i])
            # temp.pop(i)
        # 근데 닫는 괄호를 마주쳐서 pop한게 매칭되는 괄호가 아니면 바로 no 출력하고 종료
        else:
            # 스택이 존재하면
            if stack:
                if temp[i] == ']':
                    now = stack.pop()
                    if now != '[':
                        print('no')
                        yes = False
                        # temp.pop(i)
                        break
                    # else:
                    #     print('yes')
                elif temp[i] == ')':
                    now = stack.pop()
                    if now != '(':
                        print('no')
                        yes = False
                        # temp.pop(i)
                        break
                    # else:
                    #     print('yes')
            else:
                print('no')
                yes = False
                # temp.pop(i)
                break

    if yes == True:
        print('yes')