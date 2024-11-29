import sys
input = sys.stdin.readline

def ispelindrome(word):
    # 거꾸로 했을때도 똑같으면 회문이지
    return word == word[::-1]

def iskindapelindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            # 왼쪽글자를 빼보거나 오른쪽글자를 빼보거나
            skip_left = word[left+1:right+1]
            skip_right = word[left:right]
            return 1 if ispelindrome(skip_left) or ispelindrome(skip_right) else 2
        left += 1
        right -= 1
    return 2

T = int(input())

for _ in range(T):
    word = input().strip()
    if ispelindrome(word):
        print(0)
    else:
        print(iskindapelindrome(word))
