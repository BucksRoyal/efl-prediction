numbers = [12, 45, 7, 89, 34, 121, 1, 1089, 656, 301]  # list of integers
largest = numbers[0]  # assume the first number is the largest

for num in numbers:
    if num > largest:
        largest = num  # update largest if current number is bigger

print("The largest number is:", largest)
