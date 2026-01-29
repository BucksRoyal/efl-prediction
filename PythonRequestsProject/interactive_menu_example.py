"""
Simple Calculator with Menu
Demonstrates:
- while loop (main event loop)
- if-elif-else (menu choices)
- nested loops (optional repeated calculations)
"""

while True:  # Main menu loop
    print("\n--- Simple Calculator ---")
    print("1. Add two numbers")
    print("2. Multiply two numbers")
    print("3. List primes between 1 and N")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"The sum is: {a + b}")

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"The product is: {a * b}")

    elif choice == "3":
        N = int(input("List primes up to: "))
        print(f"Prime numbers up to {N}:")
        for num in range(2, N + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end=" ")
        print()  # new line after primes

    elif choice == "4":
        print("Goodbye!")
        break  # Exit the main loop

    else:
        print("Invalid choice, try again.")
