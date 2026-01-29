number = 5  # number to calculate factorial for
factorial = 1  # initialize factorial

i = 1
while i <= number:
    factorial *= i  # multiply factorial by current number
    i += 1

print(f"The factorial of {number} is {factorial}.")
