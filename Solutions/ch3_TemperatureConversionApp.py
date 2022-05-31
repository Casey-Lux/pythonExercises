# Basic manual for user
print("Welcome to Temperature conversion App!")
print("This app convert temperature in celsius degrees to fahrenheit and kelvin.")

# Data input
print("\nInput temperature in Celsius degrees pleace:")
celsius = float(input(">> "))

# Process
fahrenheit = float((celsius * 9/5) + 32)
kelvin = float(celsius + 273.15)

fahrenheit = round(fahrenheit, 4)
kelvin = round(kelvin, 4)
celsius = round(celsius, 4)

# Data output
print("celsius  |   fahrenheit  |   kelvin")
print("-----------------------------------")
print(celsius, "    |   ", fahrenheit, "    |   ", kelvin)

print("\n Thanks for use this program")
