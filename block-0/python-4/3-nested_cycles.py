from icecream import ic

print("#" * 100)
print("Nested cycles")
print("#" * 100)

matrix = [[1, 2], [3, 4], [5, 6]]
# Создаём цикл по элементам списка matrix
# row — текущее значение из списка matrix
for row in matrix:
    # Выводим содержимое на экран
    ic("Current row", row)
    # Создаём цикл по элементам списка row
    # elem — текущее значение из списка row
    for elem in row:
        ic("Current elem", elem)
    # Отделяем вывод на экран пустой строкой
    print()

print("#" * 40)
matrix = [[1, 2], [3, 4], [5, 6]]
# Вычисляем длину внешнего списка
N = len(matrix)
# Вычисляем длину вложенного списка
M = len(matrix[0])
# Создаём цикл по последовательности чисел от 0 до N (не включая N)
# i — текущий элемент последовательности (индекс строки)
for i in range(N):
    # Выводим текущее значение i
    ic("Current i", i)
    # Выводим i-е значение внешнего списка
    ic("Current row", matrix[i])
    # Создаём цикл по последовательности чисел от 0 до M (не включая M)
    # j — текущий элемент последовательности (индекс столбца)
    for j in range(M):
        # Выводим текущее значение j
        ic("Current j", j)
        # Выводим элемент под индексами i и j
        ic("Current elem", matrix[i][j])
    # Отделяем вывод на экран пустой строкой
    print()

print("#" * 40)
# Создаём список часов
hours = list(range(10, 24, 5))
# Создаём список минут
minutes = list(range(0, 60, 30))
# Создаём цикл по элементам списка часов
for hour in hours:  # hour — текущее значение часа (10, 15, 20)
    # Создаём цикл по элементам списка минут
    for minute in minutes:  # minute — текущее значение минуты
        # Выводим время
        min = "00" if minute == 0 else minute
        ic("Alarm is set {}:{}".format(hour, min))

print("#" * 40)
# Заданный список строк
str_list = ["text", "morning", "notepad", "television", "ornament"]
# Задаём начальное количество символов 'e'
count = 0
# Создаём цикл по элементам списка str_list
for text in str_list:
    # Создаём цикл по символам в строке text
    for symbol in text:
        # Проверяем условие, что текущий символ == 'e'
        if symbol == "e":
            # Если условие истинно, увеличиваем количество символов 'e'.
            count += 1
# Выводим результат
ic("Count symbol 'e':", count)

print("#" * 40)
# Заданный список строк
str_list = ["text", "morning", "notepad", "television", "ornament"]
# Задаём начальное количество символов 'e'
count = 0
# Создаём цикл по элементам списка str_list
for text in str_list:
    # Увеличиваем количество символов 'e'
    # Метод str.count() считает, сколько раз символ встречается в строке text.
    count += text.count("e")
# Выводим результат
ic("Count symbol 'e':", count)

print("#" * 40)
# Заданная матрица
random_matrix = [[9, 2, 1], [2, 5, 3], [4, 8, 5]]
# Задаём пустой список с минимальными значениями строк
min_value_rows = []
# Создаём цикл по строкам матрицы random_matrix
for row in random_matrix:  # row — текущая строка таблицы
    # Задаём начальное значение кандидата на минимум
    min_value = row[0]
    # Создаём цикл по элементам списка row
    # elem — текущий элемент из списка row
    for elem in row:
        # Проверяем условие, что текущий элемент меньше кандидата на минимум.
        if elem < min_value:
            # Если условие выполняется, заменяем кандидата на минимум.
            min_value = elem
    # Добавляем полученный минимум строки в список
    min_value_rows.append(min_value)
# Выводим минимальные элементы
ic("Minimal elements:", min_value_rows)

print("#" * 40)
# Заданная таблица со студентами
student_scores = [[56, 90, 80], [80, 86, 92], [91, 76, 89], [91, 42, 60], [65, 30, 90]]
N = len(student_scores)  # Задаём число студентов
M = len(student_scores[0])  # Задаём число экзаменов
summa = 0  # Задаём начальное значение общего балла
math_sum = 0  # Задаём начальное значение общего балла по математике
info_sum = 0  # Задаём начальное значение общего балла по информатике
rus_sum = 0  # Задаём начальное значение общего балла по русскому языку
# Создаём цикл по последовательности от 0 до N (не включая N)
for i in range(N):  # i — индекс строки
    # Добавляем баллы по математике i-го студента
    math_sum += student_scores[i][0]
    # Добавляем баллы по информатике i-го студента
    info_sum += student_scores[i][1]
    # Добавляем баллы по русскому языку i-го студента
    rus_sum += student_scores[i][2]
    # Создаём цикл по последовательности от 0 до M (не включая M)
    for j in range(M):  # j — индекс столбца
        # Добавляем баллы i-го студента по j-му экзамену
        summa += student_scores[i][j]
# Выводим средний балл по математике
ic("Average math score", math_sum / N)
# Выводим средний балл по информатике
ic("Average info score", info_sum / N)
# Выводим средний балл по русскому языку
ic("Average rus score", rus_sum / N)
# Выводим общий средний балл
ic("Average score", summa / (N * M))

print("#" * 40)
test_matrix = [[1, 2, 3, 4], [7, -1, 2, 5], [123, 2, -1, 3], [123, 5, 1]]
# Введите свое решение ниже
is_square = True
for row in test_matrix:
    if len(row) != len(test_matrix):
        is_square = False
        break
ic(is_square)
