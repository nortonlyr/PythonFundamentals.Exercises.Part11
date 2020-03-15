import uuid
import Enum

class AliveStatus(Enum):
        Decreased = 0
        Alive = 1

class Person():
        def __init__(self, first_name, last_name, dob, alive):
            self.first_name = first_name
            self.last_name = last_name
            self.dob = dob
            self.alive = alive

        def update_first_name(self, new_f_n):
            self.first_name = new_f_n

        def update_last_name(self, new_l_n):
            self.last_name = new_l_n

        def update_dob(self, new_d):
            self.dob = new_d

        def update_status(self, new_s):
            self.alive = new_s


class Instructor(Person):
        def __init__(self, instructor_id):
            self.instructor_id = "Instructor_"uuid.uuid4()
            super().__init__(first_name, last_name, dob, alive)

class Student(Person):
        def __init__(self, student_id):
            self.student_id = "Student_"uuid.uuid4()
            super.__init__(first_name, last_name, dob, alive)

class ZipCodeStudent(Student):
        def __init__(self):
            super.__init__(first_name, last_name, dob, alive)

class College_Student(Student):
        def __init__(self):
            super.__init__(first_name, last_name, dob, alive)

class Classroom():
        def __init__(self, students, instructors):
            self.students = students
            self.instrutors = instructors

        def add_instructor(a_i):
            pass

        def remove_instructor(r_i):
            pass

        def add_student(a_s):
            pass

        def remove_student(r_s):
            pass

        def print_instructor(p_i):
            pass

        def print_student(p_s):
            pass