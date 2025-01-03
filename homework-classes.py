class Person:
    def __init__(self, name, surname, gender = None):
        self.name = name
        self.surname = surname
        self.gender = gender


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


class Review(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)