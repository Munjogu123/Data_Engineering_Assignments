# Use a list comprehension to filter all the scores above 60 and store them in a new list called passed
scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]
passed = [score for score in scores if score > 60]
print(passed)

# Use another list comprehension to convert all scores into "Pass" or "Fail" using a threshold of 50.
passed_bool = ["Pass" if score >= 50 else "Fail" for score in scores]
print(passed_bool)


# Create a dictionary using comprehension that pairs each student with their mark.
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]

student_details = {student: mark for student, mark in zip(students, marks)}
print(student_details)

# Create a second dictionary that stores only students who scored more than 70
students_over_70 = {student: mark for student, mark in zip(students, marks) if mark > 70}
print(students_over_70)

# Create a third dictionary that maps each student to "Pass" or "Fail" (threshold: 50)
students_bool = {student: "Pass" if mark >= 50 else "Fail" for student, mark in zip(students, marks)}
print(students_bool)


# Write a dictionary comprehension that maps each word to its length
sentence = "Data science is fun and insightful"

sentence_dict = {sen: len(sen) for sen in sentence.split(' ')}
print(sentence_dict)
