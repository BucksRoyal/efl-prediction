numbers = [1, 3, 5, 3, 7, 3, 2]  # list of integers
count = 0  # initialize counter

for num in numbers:
    if num == 3:
        count += 1  # increment counter if number is 3

print(f"3 appears {count} times.")
