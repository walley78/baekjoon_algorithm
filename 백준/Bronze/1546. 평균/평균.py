subjectnum = int(input())
grades = list(map(int, input().split()))

maxscore = max(grades)

for idx in range(len(grades)):
    grades[idx] = grades[idx]/maxscore*100

average = sum(grades)/len(grades)

print(average)