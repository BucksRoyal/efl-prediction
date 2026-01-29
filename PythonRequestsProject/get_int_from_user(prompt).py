def get_int_from_user(prompt):
    """
    Prompt the user to enter an integer.
    Keeps asking until a valid integer is entered.
    """
    while True:
        try:
            user_input = int(input(prompt))
            return user_input  # return the integer if successful
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nInput interrupted by user. Exiting program.")
            exit()  # exit gracefully if user presses Ctrl+C


# ----------------------------
# Demo Script
# ----------------------------
if __name__ == "__main__":
    print("=== Demo: Get Integer From User ===\n")

    # Example 1: Ask for age
    age = get_int_from_user("Enter your age: ")
    print(f"Your age is {age}\n")

    # Example 2: Ask for favorite number
    favorite_number = get_int_from_user("Enter your favorite number: ")
    print(f"Your favorite number is {favorite_number}\n")

    # Example 3: Ask for any other integer
    any_number = get_int_from_user("Enter any integer: ")
    print(f"You entered: {any_number}")
