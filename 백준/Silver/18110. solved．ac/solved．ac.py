import sys

N = int(sys.stdin.readline())

if N == 0:
    print(0)
else:
    opinions = []

    for _ in range(N):
        n = int(sys.stdin.readline())
        opinions.append(n)

    # print(opinions)

    opinions.sort()

    fif = N * 0.15
    if fif - int(fif) >= 0.5:
        fif = int(fif) + 1
    else:
        fif = int(fif)

    ppl = N - (fif*2)

    if ppl == 0:
        ans = 0
    else:
        real_opinions = sum(opinions[fif:N-fif])
        ans = real_opinions/ppl
        if ans - int(ans) >= 0.5:
            ans = int(ans) + 1
        else:
            ans = int(ans)

    print(ans)
