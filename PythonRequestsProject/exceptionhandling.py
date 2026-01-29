try:
    result = 10 / 0
    print("Result is:", result)
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.", e)
finally:
    print("Execution completed.")

# Handle the second division safely
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Handled second division by zero:", e)
