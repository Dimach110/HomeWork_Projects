# Комментарии по большей части для себя, что бы потом вспомнить быстрее если потребуется,
# ну и пояснить некоторые свои отклонения от задания (так сказать лишний хлам)

class Student:
    def __init__(self, name, surname, gender, spec="Студент"):  # настроил метод инициации нового объекта
        self.name = name
        self.surname = surname
        self.gender = gender
        self.spec = spec
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):   # если честно не понял зачем здесь добавление пройденных курсов,
        self.finished_course.append(course_name)   # попало сюда из Квиза, но пусть будет

    def rate_lect(self, lecturer, course, grade):   # метод выставления оценок преподавателю
        if grade not in range(1, 11):  # Добавил условия диапазона бала, в задании об этом говорилось
            print("Студент может выставлять оценку только по 10 бальной шкале (от 1 до 10)")
        elif isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            print(f"Студент {self.name} {self.surname} не может поставить оценку преподавателю {lecturer.name} "
                  f"{lecturer.surname}, так как преподаватель не читает лекции этому студенту.")

    def average(self):  # упростил себе задачу и сделал отдельный метод подсчёта среднего бала
        sum_grades = 0
        q_grades = 0
        for grades_all in self.grades.values():
            for grade_course in grades_all:
                sum_grades += grade_course
                q_grades += 1
        return sum_grades/q_grades

    def __str__(self):  # настроил метод вызова информации по объекту
        course_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        # далее при выводе результата вызвал созданный ранее метод ср.бала self.average()
        res = f"Статус = {self.spec} \nИмя = {self.name} \nФамилия = {self.surname} " \
              f"\nСредняя оценка за лекции = {self.average():.2f} балла.  " \
              f"\nКурсы в процессе изучения: {course_in_progress} \nЗавершенные курсы: {finished_courses}"
        return res

    def __lt__(self, other):    # настроил метод сравнения объектов
        if not isinstance(other, Student):  # проверка есть ли сравниваемый объект в классе
            print(f"Студент не найден")
            return
        if self.average() > other.average(): # тут опять вызвал свой метод ср.бала
            return print(f"Студент {self.name} {self.surname} учится лучше чем студент {other.name} {other.surname}")
        else:
            return print(f"Студент {self.name} {self.surname} учится хуже чем студент {other.name} {other.surname}")

def average_all_st(l_students, course): # для задания 4 реализовал отдельную функцию (вне класса)
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
    spec = "Преподаватель"  # добавил специализацию (для себя ну и так удобнее)

    def rate_hw(self, student, course, grade):
        print(f"{self.name} {self.surname} не может ставить оценки студентам, так как он {self.spec}, а не Эксперт.")
        return "Ошибка"


class Lecturer(Mentor):     # создаём новый класс с указанием на родительский класс
    spec = "Лектор" # добавил специализацию (для себя ну и так удобнее)

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

    def __str__(self):  # настройка метода отображения информации о классе
        res = f"Статус = {self.spec} \nИмя = {self.name} \nФамилия = {self.surname} " \
              f"\nСредняя оценка за лекции = {self.average():.2f} балла."
        return res

    def __lt__(self, other):    # настройка метода сравнения преподавателя
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
    spec = "Эксперт" # добавил специализацию (для себя ну и так удобнее)

    def rate_hw(self, student, course, grade):  # метод для выставления оценок студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка выставления оценки студенту", student.name, student.surname, "за курс", course)
            return 'Ошибка'

    def __str__(self):  # настройка метода отображения информации о классе
        return f"Статус = {self.spec} \nИмя = {self.name} \nФамилия = {self.surname}"

# дальше пошли добавления объектов и загрузка данных в объекты
# данные по объекту иванов
ivanov = Student("Иван", "Иванов", "Мужчина")
ivanov.finished_courses += ["Введение в программирование"]
ivanov.courses_in_progress += ["Git"] + ["Python"]
ivanov.grades['Введение в программирование'] = [10, 10, 10, 10, 10]
ivanov.grades['Git'] = [10, 10, 10, 10]
ivanov.grades['Python'] = [10, 8, 10,]

# данные по объекту петров
petrov = Student("Пётр", "Петров", "Мужчина")
petrov.finished_courses += ["Введение в программирование"]
petrov.courses_in_progress += ["Python"] +["Git"]
petrov.grades['Введение в программирование'] = [10, 10, 8, 8, 10]
petrov.grades['Git'] = [10, 10, 8, 10]
petrov.grades['Python'] = [10, 10, 10]

# тут по приколу (не могу же себя пропустить)
chugunov = Student("Дмитрий", "Чугунов", "Мужчина")
chugunov.finished_courses += ["Git"] + ["Введение в программирование"]
chugunov.courses_in_progress += ["Python"]
chugunov.grades['Git'] = [10, 10, 10, 10, 10]
chugunov.grades['Python'] = [10, 10, 10, 10, 10]

# оставил одного преподавателя в родительском классе для проверки корректности методов
sergeev = Mentor("Сергей", "Сергеев")
sergeev.courses_attached += ["Git", "C++"]

# добавляем проверяющего преподавателя
matveev = Reviewer("Матвей", "Матвеев")
matveev.courses_attached += ["Git", "Python"]

# добавляем лектора 1
vasilev = Lecturer("Василий", "Васильев")
vasilev.courses_attached += ["Git", "Python"]

# добавляем лектора 2
andreev = Lecturer("Андрей", "Андреев")
andreev.courses_attached += ["Git", "Python"]

# ну и реального лектора как не добавить (он говорил что ему будет приятно если ему поставить за лекцию хорошую оценку),
# в netology тоже не забыл ;-)
oleg = Lecturer("Олег", "Булыгин")
oleg.courses_attached += ["Python"]

# экзаменатор оценил студентов своих курсов
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

# теперь студенты оценили преподавателей своих курсов
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
# ну и далее пошли проверки, удалять не стал что бы быстро вызвать, загнал в коммент
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
