from icecream import ic

print("#" * 40, "Default arguments", "#" * 40)

# Создадим словарь с оценками студентов
grades = {"Ivanov": 5, "Smirnov": 3, "Kuznetsova": 4, "Tihonova": 5}
# Напечатаем оценку студента, которого нет в словаре
# print(grades["Pavlov"])
# Возникнет исключение KeyError: 'Pavlov'
# Оно означает, что переданного ключа (слово "Pavlov")
# нет в словаре

print("#" * 40)
# Создадим тот же словарь
grades = {"Ivanov": 5, "Smirnov": 3, "Kuznetsova": 4, "Tihonova": 5}
# Только попробуем (try — пробовать) напечатать оценку студента,
# которого нет в словаре
try:
    ic(grades["Pavlov"])
# А если возникнет ошибка в ключе (KeyError), скажем,
# что студента нет в словаре
except KeyError:
    ic("Student’s mark was not found!")
# Будет напечатано:
# Student’s mark was not found!

print("#" * 40)


def get_time(distance, speed):
    # Если расстояние или скорость отрицательные, то возвращаем ошибку
    if distance < 0 or speed < 0:
        # Оператор raise возвращает (raise — досл. англ. "поднимать")
        # объект-исключение. В данном случае ValueError (некорректное значение).
        # Дополнительно в скобках после слова ValueError пишем текст сообщения
        # об ошибке, чтобы сразу было понятно, чем вызвана ошибка.
        raise ValueError("Distance or speed cannot be below 0!")
    result = distance / speed
    return result


# get_time(-25, 100)
# Будет напечатано:
# ValueError: Distance or speed cannot be below 0!

# get_time(50, -100)
# Будет напечатано:
# ValueError: Distance or speed cannot be below 0!


# С помощью оператора '=' присвоим
# переменной ice значение True по умолчанию
def get_cola(ice=True):
    if ice == True:
        ic("Cola with ice is ready!")
    else:
        ic("Cola without ice is ready!")


get_cola(True)
# Будет напечатано:
# Cola with ice is ready!

get_cola(False)
# Будет напечатано:
# Cola without ice is ready!

get_cola()
# Будет напечатано:
# Cola with ice is ready!


# Аргументу ice не присваиваем значение по умолчанию:
# def get_cola(ice):
#     if ice == True:
#         print("Cola with ice is ready!")
#     else:
#         print("Cola without ice is ready!")


# get_cola()
# Будет напечатано:
# TypeError: get_cola() missing 1 required positional argument: 'ice'


print("#" * 40)


# В функцию должны передаваться 2 значения:
# число и степень корня
def root(value, n):
    # Как мы уже выяснили, чтобы посчитать
    # корень степени n из числа, можно возвести это число
    # в степень 1/n
    result = value ** (1 / n)
    return result


# Посчитаем корень 3-ей степени (кубический корень) из 27
ic(root(27, 3))
# Будет напечатано:
# 3.0

print("#" * 40)


# В функцию должны передаваться 2 значения:
# число и степень корня
def root_base(value):
    # Как мы уже выяснили, чтобы посчитать
    # корень степени n из числа, можно возвести это число
    # в степень 1/n
    result = value ** (1 / 2)
    return result


# Посчитаем корень 3-ей степени (кубический корень) из 27
ic(root_base(81))
# Будет напечатано:
# 9.0

print("#" * 40, "Dangerous default arguments", "#" * 40)


# Функция add_mark (от англ. add mark — "добавить оценку")
# принимает обязательные аргументы name (имя) и
# mark (оценка). Необязательным аргументом является journal
# (журнал оценок), который по умолчанию является пустым словарём.
def add_mark(name, mark, journal={}):
    # Присваиваем имени в журнале переданную оценку
    journal[name] = mark
    return journal


# Создадим пустой словарь, в который будем
# сохранять оценки группы 1
group1 = {}
# Добавим оценки двух студентов
group1 = add_mark("Ivanov", 5, group1)
group1 = add_mark("Tihonova", 4, group1)
ic(group1)
# Будет напечатано:
# {'Ivanov': 5, 'Tihonova': 4}

# Добавим в журнал для новой группы оценку Смирнову
# Сам журнал не передаём в виде аргумента
# Пустой журнал будет использован как аргумент по умолчанию
group2 = add_mark("Smirnov", 3)
ic(group2)
# Будет напечатано:
# {'Smirnov': 3}

# Аналогично для новой группы 3 добавим оценку Кузнецовой
group3 = add_mark("Kuznetsova", 5)
ic(group3)
# Будет напечатано:
# {'Smirnov': 3, 'Kuznetsova': 5}


def add_mark_final(name, mark, journal=None):
    # Если журнал является None
    # (напоминание: сравнивать объект с None
    # корректнее через оператор is),
    # запишем в journal пустой словарь
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal


group2 = add_mark_final("Smirnov", 3)
ic(group2)
# Будет напечатано:
# {'Smirnov': 3}

group3 = add_mark_final("Kuznetsova", 5)
ic(group3)
# Будет напечатано:
# {'Kuznetsova': 5}
