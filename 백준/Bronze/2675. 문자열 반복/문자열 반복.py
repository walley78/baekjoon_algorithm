T = int(input())

for tc in range(T):
    R, S = input().split()
    R = int(R)

    for s in S:
        print(R*s, end='')
    print()