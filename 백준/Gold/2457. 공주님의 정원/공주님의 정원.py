import sys
input = sys.stdin.read

# Helper function to convert a date into "day of the year"
def day_of_year(month, day):
    # This list stores the cumulative days that have passed by the end of each month
    days_in_months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return days_in_months[month - 1] + day

# Reading all input data at once
data = input().split()
# First element is the number of flowers
N = int(data[0])
flowers = []

# Processing each flower's blooming and withering dates
for i in range(N):
    sm, sd, em, ed = map(int, data[1+4*i:5+4*i])
    # Convert start and end dates to days of the year
    start = day_of_year(sm, sd)
    end = day_of_year(em, ed) - 1  # Subtract 1 because the flower withers at the end of this day
    flowers.append((start, end))

# Sort flowers by start day, and by end day in case of ties
flowers.sort()

# Define target coverage start and end days
target_start = day_of_year(3, 1)
target_end = day_of_year(11, 30)

# Variables to keep track of the current coverage
cover_start = target_start
max_cover = 0
count = 0
i = 0
best_choice = -1

# Loop through sorted flowers to cover the target range
while i < N and cover_start <= target_end:
    updated = False
    # Loop through all flowers that start before or when the current coverage ends
    while i < N and flowers[i][0] <= cover_start:
        # Choose the flower that extends coverage the furthest
        if flowers[i][1] > max_cover:
            max_cover = flowers[i][1]
            updated = True
        i += 1
    # If we extended coverage, increment flower count and update the next required start day
    if updated:
        count += 1
        cover_start = max_cover + 1
    else:
        # No flower could extend coverage, break out of the loop
        break

# After trying to cover the range, check if we covered up to the target end day
if max_cover < target_end:
    print(0)
else:
    print(count)
