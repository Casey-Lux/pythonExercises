# h**2 = c1**2 + c2**2

# Welcome
print("\n***Welcome to the right triangle solver app***")
print("This is a program for find the hypotenuse and area for a right triangle, with its 2 bases")

# Data input
print("\n\nPlease input the firts base: ")
base1 = int(input(">> "))
print("Please enter the other base: ")
base2 = int(input(">> "))

#Process
hypotenuse = float((base1 ** 2 + base2 ** 2) ** (1/2))
area = float((base1 * base2) / 2)
hypotenuse = round(hypotenuse, 3)

# Data output
print("\nThe hypotenuse for your triangle is: ", hypotenuse)
print("The area for your triangle is: ", area)
print("\nThanks for use the program!")
