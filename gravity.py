# Gravitational constant (N·m²/kg²)
G = 6.674 * (10**-11)

# Input masses and distance
m1 = float(input("Enter the mass of the first object (kg): "))
m2 = float(input("Enter the mass of the second object (kg): "))
r = float(input("Enter the distance between the two objects (m): "))

# Calculate gravitational force
F = G * (m1 * m2) / (r**2)

# Display the result
print(f"The gravitational force between the objects is {F:.2e} N")
