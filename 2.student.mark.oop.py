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

