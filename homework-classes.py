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

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'You cannot rate lecturer for that course.'

    def average_grades(self):
        rating = 0
        length = 0
        if self.grades is None:
            return 'No grades.'
        else:
            for value in self.grades.values():
                rating += sum(value)
                length += len(value)
            rating = round(rating / length, 2)
            return rating

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.average_grades()}'
                f'\nКурсы в процессе изучения: {self.courses_in_progress}'
                f'\nЗавершенные курсы: {self.finished_courses}'
                f'\n')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Can not compare'
        return self.average_grades() < other.average_grades()


class Mentor(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        rating = 0
        length = 0
        if self.grades is None:
            return 'No grades.'
        else:
            for value in self.grades.values():
                rating += sum(value)
                length += len(value)
            rating = round(rating / length, 2)
            return rating

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.average_grades()}'
                f'\n')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Can not compare'
        return self.average_grades() < other.average_grades()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'You cannot rate student for that course.'

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\n')


# Студенты
student_1 = Student('Аскар', 'Насыров', 'М')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в программирование"]

student_2 = Student('Анастасия', 'Сина', 'Ж')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Введение в программирование"]

# Лекторы
lecturer_1 = Lecturer('Андрей', 'Быков')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Ирина', 'Попова')
lecturer_2.courses_attached += ['Python']

# Проверяющие
reviewer_1 = Reviewer('Сергей', 'Сергеев')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Ольга', 'Петровна')
reviewer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)

# Оценки лекторам
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Python', 6)

student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Python', 6)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1>student_2)