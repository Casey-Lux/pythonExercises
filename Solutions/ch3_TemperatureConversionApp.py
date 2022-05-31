# Basic manual for user
print("Welcome to Temperature conversion App!")
print("This app convert temperature in celsius degrees to fahrenheit and kelvin.")

# Data input
print("\nInput temperature in fahrenheit degrees pleace:")
fahrenheit = float(input(">> "))

# Process
celsius = float((fahrenheit - 32) * 5/9)
kelvin = float(celsius + 273.15)

fahrenheit = round(fahrenheit, 4)
kelvin = round(kelvin, 4)
celsius = round(celsius, 4)

# Data output
print("fahrenheit  |   celsius  |   kelvin")
print("-----------------------------------")
print(fahrenheit, "    |   ", celsius, "    |   ", kelvin)

print("\n Thanks for use this program")
