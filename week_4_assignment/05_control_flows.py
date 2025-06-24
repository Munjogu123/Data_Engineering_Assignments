#!/usr/bin/python3

# Write a program that checks if a number is positive, negative, or zero
def check_num(num):
    if num == 0:
        print("number is zero")
    elif num > 0:
        print("number is positive")
    else:
        print("number is negative")
        
value = int(input("Enter a number: "))
check_num(value)

# Create a program that checks if someone is eligible to vote
def vote_checker(age):
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You cannot vote")

age = int(input("Enter your age: "))  
vote_checker(age)

# Write a program that takes 3 numbers and prints the largest one
def large_num(num1, num2, num3):
    print("The largest number is:", max(num1, num2, num3))
    
large_num(12, 30, 24)

# Practice combining and, or, not
age = int(input("Enter your age: "))

if isinstance(age, int) and age > 10:
    print(age)

# Build a grading system:
# Input score (0–100)
# Output grade: A (90+), B (80–89), etc.
def grading(grade):
    if grade < 0 or grade > 100:
        print("Invalid grade")
        
    if grade >= 90:
        print("Grade A")
    elif grade >= 80:
        print("Grade B")
    elif grade >= 70:
        print("Grade C")
    elif grade >= 60:
        print("Grade D")
    else:
        print("Fail")
        
grade = int(input("Enter marks: "))
grading(grade)
