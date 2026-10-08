class Student:
    def __init__(self, name, student_id, dob):
        self._name = name
        self._dob = dob
        self._id = student_id

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def __str__(self):
        return f"Student_Id: {self._id} - Name: {self._name} - DOB: {self._dob}"

class Course:
    def __init__(self, course_id, name):
        self._id = course_id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Course_ID: {self._id} - Name: {self._name}"

class Mark:
    def __init__(self):
        self._marks = {}

    def set_mark(self, course_id, student_id, marks):
        if course_id not in self._marks:
            self._marks[course_id] = {}
        self._marks[course_id][student_id] = marks

    def get_marks(self, course_id):
        return self._marks(course_id, {})

class Management:
    def __init__(self):
        self._student = []
        self._course = []
        self.marks = Mark()

    def InputStudent(self):
        try:
            num = int(input("Input number of student: "))
            for i in range(num):
                student_id = input("Input student id: ")
                name = input("Input student name: ")
                dob = input("Input student dob: ")
                self._student.append(Student(name, student_id, dob))
        except ValueError:
            print("Not a valid number.")

    def InputCourse(self):
        try:
            num = int(input("Input number of courses:"))
            for i in range(num):
                course_id = input("Input course id: ")
                name = input("Input course name: ")
                self._course.append(Course(course_id, name))
        except ValueError:
            print("Not a valid number")

    def ListStudent(self):
        if not self._student:
            print("No student found")
            return
        for student in self._student:
            print(student)

    def ListCourse(self):
        if not self._course:
            print("No course found")
            return
        for course in self._course:
            print(course)

    def _find_student(self, student_id):
        for student in self._student:
            if student.get_id() == student_id:
                return student
        return

    def _find_course(self, course_id):
        for course in self._course:
            if course.get_id() == course_id:
                return course
        return

    def InputMark(self):
        if not self._course:
            print("No course available")
        if not self._student:
            print("No student available")

        self.ListCourse()
        course_id = input("Input course to enter mark: ").strip()
        course = self._find_course(course_id)

        if not course:
            print("Invalid course id")
            return

        for student in self._student:
            try:
                mark = float(input(f"Input mark for {Student.get_name()}: "))
                self.Mark.set_mark(course_id, Student.get_id(), mark)
            except ValueError:
                print("Invalid score")

    def ShowMark(self):
        if not self._course:
            print("No course")
            return

        course_id = input("Input course id").strip()
        course_marks = self._Mark.get_marks(course_id)
        if not mark:
            print("No mark in this course")

        for student_id, mark in course_marks.items():
            student = self._find_student(student_id)
            name = Student.get_name() if student else "unknown student"
            print(f"Id: {student_id} - Name: {name} - Mark: {mark}")

    def run(self):
        while True:
            print("1. input students")
            print("2. input courses")
            print("3. input marks for a course")
            print("4. list students")
            print("5. list courses")
            print("6. show marks for a course")
            print("0. exit")

            try:
                choice = int(input("Enter your choice "))
                if choice == 1:
                    self.InputStudent()
                elif choice == 2:
                    self.InputCourse()
                elif choice == 3:
                    self.InputMark()
                elif choice == 4:
                    self.ListStudent()
                elif choice == 5:
                    self.ListCourse()
                elif choice == 6:
                    self.ShowMark()
                elif choice == 0:
                    print("Exiting...")
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Input valid integer")

if __name__ == "__main__":
    app = Management()
    app.run()