def palin(n):
    if len(n) % 2 == 1:
        for s in range(len(n)//2):
            e = len(n)-1-s
            if n[s] != n[e]:
                return 'no'
        else:
            return 'yes'
    elif len(n) % 2 == 0:
        for s in range(len(n)//2):
            e = len(n) - 1 - s
            if n[s] != n[e]:
                return 'no'
        else:
            return 'yes'

yes = True
while yes:
    n = list(input())

    if ''.join(n) == '0':
        yes = False
        break

    result = palin(n)
    print(result)