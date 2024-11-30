import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
word3 = input().strip()

one = len(word1)
two = len(word2)
three = len(word3)

dp = [[[0]*(three+1) for _ in range(two+1)] for _ in range(one+1)]

for i in range(1, one+1):
    for j in range(1, two+1):
        for k in range(1, three+1):
            if word1[i-1] == word2[j-1] == word3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])