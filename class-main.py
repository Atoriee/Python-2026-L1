from class2 import *

students = []
courses = []
marks = {}

while True:
    print("1. input students")
    print("2. input courses")
    print("3. input marks for a course")
    print("4. list students")
    print("5. list courses")
    print("6. show marks for a course")
    print("0. exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter number of student: "))
        for i in range(num):
            print(f"Student {i+1}")
            students.append(student_info())

    elif choice == 2:
        num = int(input("Enter number of courses: "))
        for i in range(num):
            print(f"Course {i + 1}")
            courses.append(course_info())

    elif choice == 3:
        student_mark(students, courses, marks)

    elif choice == 4:
        list_student(students)

    elif choice == 5:
        list_course(courses)

    elif choice == 6:
        show_marks(students, courses, marks)

    elif choice == 0:
        print("exiting... ")
        break

    else:
        print("invalid option")