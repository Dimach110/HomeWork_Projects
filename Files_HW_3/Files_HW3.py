def file_q_line(name_file): # функция для по строчному чтению файла и подсчёту строк
    quantity_line = 0
    with open(name_file, 'r', encoding='utf-8') as file:
        for line in file:
            quantity_line += 1
    return quantity_line


def add_to_file(name_file_read, name_file_add, quantity_line):  # функция для записи данных из одного файла в общий
    with open(name_file_read, 'r', encoding='utf-8') as file_r: # открытие файла на чтение с кодированием UTF-8
        file_text = file_r.read() # чтение из файла и запись в переменную file_text
    with open(name_file_add, 'a', encoding='utf-8') as file_w: # открытие общего файла для записи в кодировании UTF-8
        file_w.write(name_file_read + '\n')     # запись в файл имени файла-источника данных
        file_w.write(quantity_line + '\n')  # запись в файл кол-ва строк
        file_w.write(file_text + '\n')  # запись в файл данных из файла исходника

# Указание имён файлов из которых берём данные
file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'

# создаём словарь с запуском функций подсчёта кол-ва строк
text_line = {file1: file_q_line(file1), file2: file_q_line(file2), file3: file_q_line(file3)}
sort_text_line = sorted(text_line.items(), key=lambda x: x[1]) # переводим в кортеж и сортируем по значению (кол-во строк)
text_line = dict(sort_text_line) # возвращаем в словарь
for file_n, q_line in text_line.items():    # Запускаем цикл для поочерёдного запуска функции записи в общий файл
    add_to_file(file_n, 'all_text.txt', str(q_line))

