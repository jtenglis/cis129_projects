# Author: JT Englis
# Title: Module 11: Lab - 9.1 Writing Grades to a Plain Text File
# Date: 12/1/2024

# Writing grades to a text file
grades_file = "grades.txt"

# Open the file in write mode
with open(grades_file, "w") as file:
    while True:
        grade = input("Enter a grade (or type 'done' to finish): ")
        if grade.lower() == 'done':
            break
        if grade.isdigit():  # Ensure valid grades
            file.write(grade + '\n')
        else:
            print("Invalid grade. Please enter a number.")
print(f"Grades have been written to {grades_file}.")
