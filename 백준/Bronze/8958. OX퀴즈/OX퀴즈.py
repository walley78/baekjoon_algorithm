T = int(input())

for tc in range(T):
    ox = list(input())
    stack = []
    score = 0
    for i in range(len(ox)):
        if not stack and ox[i] == "O":
            stack.append(1)
        elif stack and ox[i] == "O":
            stack.append(stack[-1] + 1)
        if ox[i] == "X":
            while stack:
                accumulate = stack.pop()
                score += accumulate
    while stack:
        accum = stack.pop()
        score += accum

    print(score)