H, M = map(int, input().split())

total_minutes = H * 60 + M
adjusted_minutes = (total_minutes - 45 + 1440) % 1440

adjusted_hours, adjusted_minutes = divmod(adjusted_minutes, 60)

print(adjusted_hours, adjusted_minutes)