weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height**2)

# Determine BMI category
if bmi < 18.5:
    print("Underweight.")
elif 18.5 <= bmi < 25:
    print("Normal weight.")
elif 25 <= bmi < 30:
    print("Overweight.")
else:
    print("Obese.")

# Optional: print BMI value rounded to 2 decimals
print(f"Your BMI is: {bmi:.2f}")
