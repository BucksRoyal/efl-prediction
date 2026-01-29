real1 = float(input("Enter the real part of the first number: "))
imag1 = float(input("Enter the imaginary part of the first number: "))

# Ask user for the second complex number
real2 = float(input("Enter the real part of the second number: "))
imag2 = float(input("Enter the imaginary part of the second number: "))

# Create complex numbers
num1 = complex(real1, imag1)
num2 = complex(real2, imag2)

# Subtract the complex numbers
difference = num1 - num2

print(f"Difference: {difference}")
