val = int(input("Enter an integer: "))

# print if the val is even or odd
for val in range(1, 201):
    if val % 2 == 0:
        print(val, "is even")
    else:
        print(val, "is odd")

# Find the first prime number between 100 and 200
for num in range(101, 201):  # Start from 101
    is_prime = True  # Assume it is prime

    # Check divisibility from 2 up to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False  # Found a factor → not prime
            break  # Stop checking this number

    if is_prime:
        print(f"The first prime number between 100 and 200 is: {num}")
        break  # Stop the entire loop as soon as we find the first prime
