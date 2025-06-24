#!/usr/bin/python3

# Create a list of 5 fruits and print the third fruit.
fruits = ["orange", "apple", "banana", "pear", "citrus"]
print(fruits[2])

# Create a dictionary with keys: name, age. Print the value of age
values = {'name': 'Fred', 'age': 22}
print(values['age'])

# Define a tuple with three numbers. Try modifying it. What happens?
locations = ('Nrb', 'Msa', 'Eld')
# locations[1] = 'Nkr' # you get an error saying that tuples do not support modification/mutation

# Create a set from a list with duplicate values
marks = [70, 98, 23, 70, 58, 98, 58, 23]
unique_marks = set(marks)
print(unique_marks)

# Create a program that:
# Takes 5 user inputs and stores them in a list
# Converts the list into a set and prints the unique values
value_1 = input("Enter the name of a sport: ")
value_2 = input("Enter the name of a sport: ")
value_3 = input("Enter the name of a sport: ")
value_4 = input("Enter the name of a sport: ")
value_5 = input("Enter the name of a sport: ")

value_list = [value_1, value_2, value_3, value_4, value_5]
print(value_list)
value_unique = set(value_list)
print(value_unique)
