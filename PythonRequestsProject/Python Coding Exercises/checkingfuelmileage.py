distance_km = float(input("Enter the distance traveled in kilometers: "))
fuel_liters = float(input("Enter the fuel used in liters: "))

# Calculate mileage
mileage = distance_km / fuel_liters  # km per liter

# Print mileage rounded to 2 decimal places
print(f"Mileage: {mileage:.2f} km per liter")
