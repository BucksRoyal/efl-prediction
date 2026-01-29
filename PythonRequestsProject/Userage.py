while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
        break  # exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a number.")
    except KeyboardInterrupt:
        print("\nInput interrupted by user. Exiting program.")
        exit()  # stop the program gracefully

print("\n--- Part 2: Safe Division Function ---")


# --- Part 2: Safe Division Function ---
def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None


# Division input
try:
    num1 = float(input("Enter numerator for division: "))
    num2 = float(input("Enter denominator for division: "))
    result = safe_divide(num1, num2)
    if result is None:
        print("Cannot divide by zero!")
    else:
        print(f"Result of division: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except KeyboardInterrupt:
    print("\nInput interrupted by user. Skipping division.")

print("\n--- Part 3: Read Numbers from File ---")

# --- Part 3: Read numbers from a file safely ---
file_name = input("Enter the filename to read numbers from: ")
numbers = []

try:
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            numbers.append(float(line))  # may raise ValueError
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except ValueError as e:
    print(f"Error: Cannot convert line to number. {e}")
else:
    print("Numbers successfully read:", numbers)
finally:
    print("File processing complete.")
