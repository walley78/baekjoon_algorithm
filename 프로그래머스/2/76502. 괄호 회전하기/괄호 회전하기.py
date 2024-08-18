def solution(s):
    cnt = 0
    def isright(brackets):
        stack = []
        for i in brackets:
            if i in {'[', '{', '('}:
                stack.append(i)
            else:
                if stack:
                    if i == '}' and stack[-1] == '{':
                        stack.pop()
                    elif i == ']' and stack[-1] == '[':
                        stack.pop()
                    elif i == ')' and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        else:
            if stack:
                return False
            else:
                return True
        
    for i in range(len(s)):
        if i == 0:
            if isright(s):
                cnt += 1
        else:
            new_s = s[i:] + s[:i]
            if isright(new_s):
                cnt += 1
    return cnt