secret_number = 4  # the number to guess
guess = None  # initialize the guess variable

while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Correct!")
