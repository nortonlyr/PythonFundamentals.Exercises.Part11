import uuid
from enum import Enum
from typing import List, Dict

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus.Alive

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob:str):
        self.dob = dob

    def update_status(self, alive: AliveStatus):
        self.alive = alive


class Instructor(Person):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.instructor_id = f"Instructor_{uuid.uuid4()}"


class Student(Person):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.student_id = f"Student_{uuid.uuid4()}"


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)


class CollegeStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)


class GradeBook:
    pass


class Classroom:
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.instructors: Dict[str, Instructor] = {}

    def add_instructor(self, instructor: Instructor):
        self.instructors[instructor.instructor_id] = instructor

    def remove_instructor(self, instructor:Instructor):
        if instructor.instructor_id in self.instructors:
            del self.instructors[instructor.instructor_id]

    def add_student(self, student: Student):
        self.students[student.student_id] = student

    def remove_student(self, student):
        if student.student_id in self.students:
            del self.students[student.student_id]

    def print_instructors(self):
        for key, value in self.instructors.items():
            print(f"{key}: {value}")

    def print_students(self):
        for key, value in self.students.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    pass