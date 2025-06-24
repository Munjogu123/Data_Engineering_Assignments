#!/usr/bin/python3

# Use a for loop to print numbers from 1 to 10
for i in range(1, 11):
    if i < 10:
        print(i, end=',')
    else:
        print(i)

# Use a while loop to print numbers until the user enters stop
value = input("Enter a command: ")

i = 22

while value != 'stop':
    print(i)
    i += 1
    value = input("Enter a command: ")

# Write a loop that prints even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        if i < 20:
            print(i, end=',')
        else:
            print(i)

# Explain what break and continue do in your own words
""" break - exits the loop when a certain condition is met or the program executes the break statement """
""" continue - it skips a certain execution if it meets the condition but still continues with the loop """


# Write a guessing game that asks the user to guess a secret number between 1 and 10.
# Give feedback (too high / too low)
# Use a while loop
secret_num = 8

while True:
    guess = input("Guess a number: ")
    guess = int(guess)
    
    if guess > secret_num:
        print("Too high")
    elif guess < secret_num:
        print("Too low")
    else:
        print("Hooray!")
        break
