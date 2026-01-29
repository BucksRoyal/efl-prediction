principal = float(input("Enter the principal amount (£): "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))

# Simple Interest formula: SI = (P * R * T) / 100
interest = (principal * rate * time) / 100

print(f"Interest earned: £{interest:.2f}")
