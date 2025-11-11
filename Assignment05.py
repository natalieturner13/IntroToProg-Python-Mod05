# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Natalie Turner,11/10/2025, Started Assignment
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
except FileNotFoundError as e:
    print("File not found")
    print("Technical error details:", e)
except Exception as e:
    print("Unexpected error")
    print("Technical error details:", e)

while True:

    print (MENU)
    menu_choice = input("Enter your choice: ")

    if menu_choice == '1':
        try:
            student_first_name = input("Enter your first name: ")
            if not student_first_name.isalpha():
                raise ValueError ("First name must contain only letters")
            student_last_name = input("Enter your last name: ")
            if not student_last_name.isalpha():
                raise ValueError ("Last name must contain only letters")
            course_name = input("Enter your course name: ")
            student_data = {
                "first_name": student_first_name,
                "last_name": student_last_name,
                "course_name": course_name,
            }
            students.append(student_data)
        except ValueError as e:
            print("Invalid input")
            print("Technical error details:", e)
        except Exception as e:
            print("Unexpected error")
            print("Technical error details:", e)
    elif menu_choice == '2':
        for student_data in students:
            student_first_name = student_data['first_name']
            student_last_name = student_data['last_name']
            course_name = student_data['course_name']
            print(f'{student_first_name}, {student_last_name}, {course_name}')
    elif menu_choice == '3':
        try:
            file = open(FILE_NAME, 'w')
            json.dump(students, file)
            file.close()
            print("The following data has been saved to Enrolments.json: " + f"{students}")
        except Exception as e:
            print("Unexpected error")
            print("Technical error details:", e)
    elif menu_choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
