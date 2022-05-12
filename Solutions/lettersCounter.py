# Variables definition
letter = 'a'
phrase = "example"
counter = 0

# Data enter

print("Hello, this is a program for count letters in a phrase.")
print("Please, enter a phrase:")
phrase = input(">> ")

print("Ok, now please enter the letter that you want to count in the phrase:")
letter = input(">> ")

# Proces

for i in phrase:
    if (i == letter):
        counter = (counter + 1)

# Print data

print("In the phrase '" + phrase + "' there is your choosen letter:")
print(counter, "times.")
print("Thanks for use the program!")