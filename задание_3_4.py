
# Задание 3


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            for one_grade in grades_list:
                all_grades.append(one_grade)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self._avg_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    # Сравнение студентов
    def __lt__(self, other):
        if isinstance(other, Student):
            return self._avg_grade() < other._avg_grade()
        raise TypeError

    def rate_lecture(self, lecturer, course, grades):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and
                course in self.courses_in_progress and 1 <= grades <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            for one_grade in grades_list:
                all_grades.append(one_grade)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self._avg_grade():.1f}")

    # Сравнение лекторов
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._avg_grade() < other._avg_grade()
        raise TypeError


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()


# Задание 4. Создайте по 2 экземпляра каждого класса, вызовите все созданные методы:

# экземпляры лекторов
lecturer_1 = Lecturer('Максим', 'Максимов')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Денис', 'Денисов')
lecturer_2.courses_attached += ['Python']

# экземпляры проверяющих
reviewer_1 = Reviewer('Павел', 'Павлов')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Антон', 'Антонов')
reviewer_2.courses_attached += ['Python']

# экземпляры студентов
student_1 = Student('Роксана', 'Бабаян', 'ж')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Евгений', 'Петросян', 'м')
student_2.courses_in_progress += ['Python']

# вызов методов

# Проверяющие ставят оценки
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)

# Студенты ставят оценки
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_1, 'Python', 9)

# Перезагрузка __str__
print("Результат работы __str__ для Reviewer:")
print(reviewer_1)

print("\nРезультат работы __str__ для Lecturer:")
print(lecturer_1)

print("\nРезультат работы __str__ для Student:")
print(student_1)


# Сравнение __lt__
print("\nСравнение студентов (student_1 > student_2):")
print(student_1 > student_2)  # Вызовет __lt__ внутри

print("\nСравнение лекторов (lecturer_1 < lecturer_2):")
print(lecturer_1 < lecturer_2)


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def avg_hw_grade_course(students_list, course_name):
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def avg_lecture_grade_course(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if not all_grades:
        return 0
    return sum(all_grades) / len(all_grades)

# Проверка функций
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

avg_students_python = avg_hw_grade_course(students, 'Python')
print(f"Средняя оценка студентов за ДЗ по курсу Python: {avg_students_python:.1f}")
avg_lecturers_python = avg_lecture_grade_course(lecturers, 'Python')
print(f"Средняя оценка лекторов за лекции по курсу Python: {avg_lecturers_python:.1f}")