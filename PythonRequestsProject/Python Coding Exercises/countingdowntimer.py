# Example 1: Timer countdown
timer = 5  # integer variable

while timer > 0:
    print(timer)
    timer -= 1
else:
    print("Timer complete!")

# Example 2: Odd or even check with user input
number = int(input("\nEnter a number: "))  # ask the user to input a number

if number % 2 == 0:
    print("The number is even.")
elif number % 2 != 0:
    print("The number is odd.")

# Example 3: Countdown from that number if it's even
if number % 2 == 0:
    print("\nCountdown from the number:")
    while number > 0:
        print(number)
        number -= 1
    else:
        print("Countdown complete!")
