# input_output.py
# Goal: practice input(), converting types, and clean output.

# TASK 1:
# Ask the user for their first name and last name, then print:
# "Hello, <first> <last>!"
first = input("First Name: ")
last = input("Last name: ")

print(f"Hello, {first} {last}!")
# TASK 2:
# Ask the user for two numbers (as input), convert them to integers,
# then print their sum.
a = int(input("Number 1: "))
b = int(input("Number 2: "))
print("Sum: ",a + b)
# TASK 3:
# Ask the user for their age (input), convert to int,
# then print how old they will be next year.
age = int(input("Age: "))
print("Next year you will be:", age + 1)
# Start here:
# Write your solutions below this line.
