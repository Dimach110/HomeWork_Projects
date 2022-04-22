class Student:
    def __init__(self, name, surname, gender, spec="Студент"):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.spec = spec
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if grade not in range(1, 11):
            print("Студент может выставлять оценку только по 10 бальной шкале (от 1 до 10)")
        elif isinstance(lecturer,
                        Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            print(f"Студент {self.name} {self.surname} не может поставить оценку преподавателю {lecturer.name} "
                  f"{lecturer.surname}, так как преподаватель не читает лекции этому студенту.")

    def average(self):
        sum_grades = 0
        q_grades = 0
        for grades_all in self.grades.values():
            for grade_course in grades_all:
                sum_grades += grade_course
                q_grades += 1
        return sum_grades/q_grades

    def __str__(self):
        course_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        res = f"Статус = {self.spec} \nИмя = {self.name} \nФамилия = {self.surname} " \
              f"\nСредняя оценка за лекции = {self.average():.2f} балла. " \
              f"\nКурсы в процессе изучения: {course_in_progress} \nЗавершенные курсы: {finished_courses}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f"Студент не найден")
            return
        if self.average() > other.average():
            return print(f"Студент {self.name} {self.surname} учится лучше чем студент {other.name} {other.surname}")
        else:
            return print(f"Студент {self.name} {self.surname} учится хуже чем студент {other.name} {other.surname}")

def average_all_st(l_students, course):
    all_grades = 0
    q_grades = 0
    for student in l_students:
        for course_grade in student.grades[course]:
            all_grades +=course_grade
            q_grades += 1
    return print(f'Средняя оценка студентов по курсу {course} составляет {all_grades/q_grades:.2f} бала')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    spec = "Преподаватель"

    def rate_hw(self, student, course, grade):
        print(f"{self.name} {self.surname} не может ставить оценки студентам, так как он {self.spec}, а не Эксперт.")
        return "Ошибка"


class Lecturer(Mentor):
    spec = "Лектор"

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def average(self):
        sum_grades = 0
        q_grades = 0
        for grades_all in self.grades_lecturer.values():
            for grade_course in grades_all:
                sum_grades += grade_course
                q_grades += 1
        return sum_grades/q_grades

    def __str__(self):
        res = f"Статус = {self.spec} \nИмя = {self.name} \nФамилия = {self.surname} " \
              f"\nСредняя оценка за лекции = {self.average():.2f} балла."
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f"Такой преподаватель не найден")
            return
        if self.average() > other.average():
            return print(f"Преподаватель {self.name} {self.surname} читает лекции лучше чем преподаватель {other.name} {other.surname}")
        else:
            return print(f"Преподаватель {self.name} {self.surname} читает лекции лучше чем преподаватель {other.name} {other.surname}")

def average_all_lect(l_lector, course):
    all_grades = 0
    q_grades = 0
    for lector in l_lector:
        for course_grade in lector.grades_lecturer[course]:
            all_grades +=course_grade
            q_grades += 1
    return print(f'Средняя оценка лекторов по курсу {course} составляет {all_grades/q_grades:.2f} бала')

class Reviewer(Mentor):
    spec = "Эксперт"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка выставления оценки студенту", student.name, student.surname, "за курс", course)
            return 'Ошибка'

    def __str__(self):  # Задаём магический метод для нужного нам вывода данных при print(преподаватель)
        return f"Статус = {self.spec} \nИмя = {self.name} \nФамилия = {self.surname}"

ivanov = Student("Иван", "Иванов", "Мужчина")
ivanov.finished_courses += ["Введение в программирование"]
ivanov.courses_in_progress += ["Git"] + ["Python"]
ivanov.grades['Введение в программирование'] = [10, 10, 10, 10, 10]
ivanov.grades['Git'] = [10, 10, 10, 10]
ivanov.grades['Python'] = [10, 8, 10,]


petrov = Student("Пётр", "Петров", "Мужчина")
petrov.finished_courses += ["Введение в программирование"]
petrov.courses_in_progress += ["Python"] +["Git"]
petrov.grades['Введение в программирование'] = [10, 10, 8, 8, 10]
petrov.grades['Git'] = [10, 10, 8, 10]
petrov.grades['Python'] = [10, 10, 10]

chugunov = Student("Дмитрий", "Чугунов", "Мужчина")
chugunov.finished_courses += ["Git"] + ["Введение в программирование"]
chugunov.courses_in_progress += ["Python"]
chugunov.grades['Git'] = [10, 10, 10, 10, 10]
chugunov.grades['Python'] = [10, 10, 10, 10, 10]

sergeev = Mentor("Сергей", "Сергеев")
sergeev.courses_attached += ["Git", "C++"]

matveev = Reviewer("Матвей", "Матвеев")
matveev.courses_attached += ["Git", "Python"]

vasilev = Lecturer("Василий", "Васильев")
vasilev.courses_attached += ["Git", "Python"]

andreev = Lecturer("Андрей", "Андреев")
andreev.courses_attached += ["Git", "Python"]

oleg = Lecturer("Олег", "Булыгин")
oleg.courses_attached += ["Python"]

matveev.rate_hw(ivanov, "Python", 6)     # для проверки
matveev.rate_hw(petrov, "Python", 6)     # Эксперт поставил студенту Петрову 3 за ДЗ
matveev.rate_hw(ivanov, "Git", 8)     # для проверки
matveev.rate_hw(petrov, "Git", 8)     # Эксперт поставил студенту Петрову 3 за ДЗ
matveev.rate_hw(chugunov, "Python", 10)  # Эксперт поставил за ДЗ Чугунову 10, потому что МОЛОДЕЦ! :-)

# sergeev.rate_hw(ivanov, "Python", 3) # для проверки
# sergeev.rate_hw(petrov, "Python", 3) # для проверки
# sergeev.rate_hw(ivanov, "Git", 3) # для проверки
# sergeev.rate_hw(petrov, "Git", 3) # для проверки

# vasilev.rate_hw(petrov, "Python", 3) # для проверки

# ivanov.rate_lect(vasilev, "Python", 10) # для проверки
# vasilev.grades_lecturer["Python"] = [7] # для проверки

petrov.rate_lect(vasilev, "Python", 8)  # Петров оценил лектора Васильева за лекцию по Python
petrov.rate_lect(vasilev, "Python", 6)
petrov.rate_lect(vasilev, "Python", 4)
ivanov.rate_lect(vasilev, "Git", 10)    # Иванов оценил лектора Васильева за лекцию по Git
ivanov.rate_lect(vasilev, "Git", 8)
ivanov.rate_lect(vasilev, "Git", 7)
petrov.rate_lect(andreev, "Python", 10)  # Петров оценил лектора Васильева за лекцию по Python
petrov.rate_lect(andreev, "Python", 8)
petrov.rate_lect(andreev, "Python", 10)
ivanov.rate_lect(andreev, "Git", 10)    # Иванов оценил лектора Васильева за лекцию по Git
ivanov.rate_lect(andreev, "Git", 10)
ivanov.rate_lect(andreev, "Git", 6)

chugunov.rate_lect(oleg, "Python", 10)  # Чугунов оценил лектора Олега по максимальной оценке
chugunov.rate_lect(oleg, "Python", 10)  # Чугунов оценил лектора Олега по максимальной оценке 2 раза
#
# print(ivanov.__dict__)
# print(petrov.__dict__)
# # print(chugunov.__dict__)
# # print(sergeev.__dict__)
# print(matveev.__dict__)
# print(vasilev.__dict__)
# # print(oleg.__dict__)
# # print()
# # print(matveev)
# print()
# print(vasilev)
# print()
# print(ivanov)
# print()
# print(petrov)
# print()
#
# ivanov.__lt__(petrov)
# print()
# andreev.__lt__(vasilev)

print("_"*100)
average_all_st([ivanov, petrov], "Python")
average_all_lect([andreev,vasilev], "Python")
