# Author: JT Englis
# Title: Module 11: Lab - 9.3 Writing Student Records to a CSV File
# Date: 12/1/2024

import csv

# Writing student records to a CSV file
csv_file = "grades.csv"

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["firstname", "lastname", "exam1grade", "exam2grade", "exam3grade"])
    
    while True:
        firstname = input("Enter the student's first name (or type 'done' to finish): ")
        if firstname.lower() == 'done':
            break
        lastname = input("Enter the student's last name: ")
        try:
            exam1 = int(input("Enter exam 1 grade: "))
            exam2 = int(input("Enter exam 2 grade: "))
            exam3 = int(input("Enter exam 3 grade: "))
            # Write the student record to the CSV file
            writer.writerow([firstname, lastname, exam1, exam2, exam3])
        except ValueError:
            print("Invalid input. Please enter integer values for grades.")
print(f"Student records have been written to {csv_file}.")
