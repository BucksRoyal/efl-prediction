# Odd or Even Check (User Input 1-100)

while True:
    try:
        number = int(input("Enter a number between 1 and 100: "))
        if 1 <= number <= 100:
            break  # valid input, exit loop
        else:
            print("Invalid input. Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Check if the number is odd or even
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
