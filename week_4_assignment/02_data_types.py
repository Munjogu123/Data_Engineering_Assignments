#!/usr/bin/python3

# Print the type of 42, 3.14, and 'hello'
print(type(42))
print(type(3.14))
print(type('hello'))

# Convert a string '100' to an integer
number = '100'
new_num = int(number)
print(new_num)
print(type(new_num))

# Add an integer and a float together. What is the result?
print(1 + 3.14) # the result is a float

# What happens when you try to multiply a string by a number?
print('Hello' * 3) # it prints the number n number of times


# Write a program that:
# Asks the user to enter two numbers (as strings)
# Converts them to integers or floats
# Prints their sum and type
num_1 = input("Enter a number: ")
num_2 = input("Enter a number: ")

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)
print(type(num_1 + num_2))
