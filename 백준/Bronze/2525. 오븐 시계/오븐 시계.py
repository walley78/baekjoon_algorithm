current_hr, current_min = map(int, input().split())
oven_time = int(input())

current_time = current_hr*60 + current_min
total_time = current_time + oven_time

cook_hr = total_time//60
cook_min = total_time - cook_hr*60

if cook_hr >= 24:
    cook_hr -= 24

print(f"{cook_hr} {cook_min}")