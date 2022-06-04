#Welcome to user
print("Welcome to multiplication and exponent table app!")
print("This program makes a multiplication and exponent table with a number that you enter")

#Data input
print("Please, enter a number: ")
number = int(input(">> "))

#Process
print("\n***Multiplication Table***\n")
for i in range(1, 10):
    result = int(number * i)
    print(number, " * ", i, " = ", result)
    
print("\n***Exponent Table***\n")
for i in range(1, 10):
    result = int(number ** i)
    print(number, " ^ ", i, " = ", result)

print("\nMathematics are great!")
print("Mathematics are very cool!!!")
print("MATHEMATICS ARE VERY VERY COOL!!!!")
