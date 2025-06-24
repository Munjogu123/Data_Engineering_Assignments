#!/usr/bin/python3

# Write a function greet(name) that prints “Hello, [name]”
def greet(name):
    print(f"Hello, {name}")
    
greet('Fred')

# Create a function add(a, b) that returns the sum
def add(a, b):
    return a + b

print(add(2, 3))

# Modify add() to print “even” or “odd” based on the result
def add_mod(a, b):
    answer = a + b
    if answer % 2 == 0:
        print("even")
    else:
        print("odd")
        
add_mod(2, 3)

def total_salary(base_salary, bonus):
    full_salary = add(base_salary, bonus)
    return full_salary

print(total_salary(10000, 5000))

# Write a calculator function:
# Takes two numbers and an operation (+, -, *, /)
# Returns the result
def calc(num1, num2, operation):
    ops = ['+', '-', '*', '/']
    if operation not in ops:
        return f"{operation} is not a valid operation"
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    else:
        return num1 / num2
    
print(calc(10, 3, '+'))
