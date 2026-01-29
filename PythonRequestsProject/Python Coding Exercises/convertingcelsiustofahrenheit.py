celsius = float(input("Enter the temperature in Celsius: "))

# Check if the temperature is valid (above absolute zero)
if celsius >= -273.15:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit}.")
else:
    print("Invalid temperature! Cannot be below absolute zero.")
