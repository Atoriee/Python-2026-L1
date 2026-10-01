from math import floor

def student_info():
    name = input("input name: ")
    student_id = input("input student_id: ")
    dob = input("input date_of_birth: ")
    return {"name": name, "id": student_id, "dob": dob}

def course_info():
    course_id = input("input course id: ").strip()
    name = input("input course name: ")
    return {"course": name, "id": course_id}

def student_mark(students, courses, marks):
    if not courses:
       print("no course")
       return
    if not students:
       print("no student")
       return
    for course in courses:
       print(f"{course['id']} - {course['course']}")
    course_id = input("input course_id to choose the course").strip()

    if not any(c["id"] == course_id for c in courses):
       print("invalid course")
       return

    if course_id not in marks:
       marks[course_id] = {}

    print(f"\nEnter mark for course: {course_id}")
    for student in students:
        mark = float(input(f"Enter mark for {student["name"]}: "))
        marks[course_id][student["id"]] = mark

def list_course(courses):
    print("list of courses: ")
    if not courses:
       print("no course")
       return
    for course in courses:
       print(f"ID: {course['id']} - Name: {course['course']}")

def list_student(students):
   print("list of students: ")
   if not students:
      print("no student")
      return
   for student in students:
      print(f"name: {student["name"]} - student_id: {student["id"]} - dob: {student["dob"]}") 

def show_marks(students, courses, marks):
    if not courses:
       print("no course")
       return

    course_id = input("input course id: ")
    if course_id not in marks:
       print("no mark in this course")
       return

    for course in courses:
       print(f"{course['id']} - {course['course']}")

    find = {s["id"] : s["name"] for s in students}
    print(f"\nmark for course {course_id}")
    for student_id, mark in marks[course_id].items():
       name = find.get(student_id, "no student")
       print(f"id: {student_id} - name: {name} - mark: {floor(mark)}")