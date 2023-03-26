from enum import Enum
from uuid import UUID


class AliveStatus(Enum):
    deceased = 0
    alive = 1

class Person:

    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_status):
        self.alive = new_status


class Instructor(Person):
    def __init__(self, first_name, last_name, dob, instructor_id):
        self.instructor_id = f'Instructor_{instructor_id}{UUID()}'
        super().__init__(first_name, last_name, dob)

class Student(Person):
    def __init__(self, first_name, last_name, dob, student_id):
        self.student_id = f'Student_{student_id}{UUID()}'
        super().__init__(first_name, last_name, dob)

class ZipCodeStudent(Student):
    def __int__(self, first_name, last_name, dob, student_id):
        super().__init__(first_name, last_name, dob, student_id)

class Classroom():
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, new_instructor):
        self.instructors.append(new_instructor)

    def remove_instructor(self):
        self.instructors.remove(new_instructor)


    def add_student(self, new_student):
        self.students.append(new_student)


    def remove_student(self, new_student):
        self.students.remove(new_student)

    def print_instructors(self):
        for i in self.instructors:
            print(i)

    def print_students(self):
        for i in self.students:
            print(i)












