def student_info():
    name = input("input name: ")
    student_id = input("input student_id: ")
    dob = input("input date_of_birth: ")
    return {"name": name, "id": student_id, "dob": dob}

def course_info():
    course_id = input("input course id: ")
    course = input("input course name: ")
    return (course_id, course)

def student_mark(students, courses, marks):
    if not courses:
       print("no course")
       return
    elif not students:
       print("no student")
       return
    for cid, cname in courses:
       print(f"{cid} - {cname}")
    course_id = input("input course_id to choose the course")

    available = any(c[0] == course_id for c in courses)
    if not available:
       print("invalid course")
       return

    if course_id not in marks:
       marks[course_id] = {}

    print(f"\nEnter mark for course: {course_id}")
    for student in students:
        mark = float(input(f"Enter mark for {student["name"]}: "))
        mark[course_id][student["id"]] = marks

def list_course(courses):
    print("list of courses: ")
    if not courses:
       print("no course")
       return
    for cid, cname in courses:
       print(f"ID: {cid} - Name: {cname}")

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

    course_id = int(input("input course id: "))
    if course_id not in marks:
       print("no mark in this course")
       return

    find = {s["id"] : s["name"] for s in students}
    print(f"\nmark for course {course_id}")
    for student_id, mark in marks[course_id].item():
       name = find.get(student_id, "no student")
       print(f"id: {student_id} - name: {name} - mark: {mark}")