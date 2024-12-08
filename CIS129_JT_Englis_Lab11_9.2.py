# Author: JT Englis
# Title: Module 11: Lab - 9.2 Reading Grades from a Plain Text File
# Date: 12/1/2024

# Reading grades from the text file
grades_file = "grades.txt"

try:
    with open(grades_file, "r") as file:
        grades = [int(line.strip()) for line in file]
        if grades:
            print("Grades:", grades)
            total = sum(grades)
            count = len(grades)
            average = total / count
            print(f"Total: {total}, Count: {count}, Average: {average:.2f}")
        else:
            print("No grades available in the file.")
except FileNotFoundError:
    print(f"The file {grades_file} does not exist.")
