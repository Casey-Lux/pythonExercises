# Defining variables

milesPerHour = float()
metersPerSecond = float()

# Data introduction

print("Hello, this is a program for convert miles per hour to meters per second.")
print("Please enter a speed in miles per hour:")
milesPerHour = float(input(">> "))

# Proces

metersPerSecond = float(milesPerHour * 0.447)
metersPerSecond = round(metersPerSecond, 2)

# Data exit

print(milesPerHour, "mph =", metersPerSecond, "m/s.")
print("End of program, thanks for use me!")
