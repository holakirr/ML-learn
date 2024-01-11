from icecream import ic

print("#" * 100)
print("Advanced arguments handling")
print("#" * 100)

print("#" * 40, "*args", "#" * 40)


# В массив args будут записаны все переданные
# порядковые аргументы
def mean(*args):
    # Среднее значение — это сумма всех значений,
    # делённая на число этих значений
    # Функция sum — встроенная, она возвращает
    # сумму чисел
    result = sum(args) / len(args)
    return result


# Передадим аргументы в функцию через запятую,
# чтобы посчитать их среднее
ic(mean(5, 4, 4, 3))
# Будет напечатано
# 4.0

print("#" * 40)


def mean(*numbers):
    result = sum(numbers) / len(numbers)
    return result


ic(mean(5, 4, 4, 3))
# Будет напечатано
# 4.0

print("#" * 40, "What is *args?", "#" * 40)


def mean(*args):
    ic(isinstance(args, tuple))
    result = sum(args) / len(args)
    return result


ic(mean(1, 2, 3))

print("#" * 40)


# В качестве первого аргумента принимаем фамилию
# студента, а затем уже его оценки через запятую
def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    # Не возвращаем результат, а печатаем его
    ic(name + ":", result)


mean_mark("Ivanov", 5, 5, 5, 4)
mean_mark("Petrov", 5, 3, 5, 4)
# Будет напечатано:
# Ivanov: 4.75
# Petrov: 4.25


# Поменяем местами *marks, name
def mean_mark_wrong(*marks, name):
    result = sum(marks) / len(marks)
    ic(name + ":", result)


# mean_mark_wrong(5, 5, 5, 4, "Ivanov")
# Будет напечатано:
# TypeError: mean_mark_wrong() missing 1 required keyword-only argument: 'name'

# Воспользуемся названием name, чтобы передать фамилию
# в этот аргумент
mean_mark_wrong(5, 5, 5, 4, name="Ivanov")
# Будет напечатано:
# Ivanov: 4.75

print("#" * 40, "*args as an argument", "#" * 40)
langs = ["Python", "SQL", "Machine Learning", "Statistics"]
print(langs)
# Будет напечатано:
# ['Python', 'SQL', 'Machine Learning', 'Statistics']
print(*langs)
# Будет напечатано:
# Python SQL Machine Learning Statistics

print("#" * 40)

# Должно быть напечатано:
# Python, SQL, Machine Learning, Statistics
print(*langs, sep=", ")

print("#" * 40)
marks = [4, 5, 5, 5, 5, 3, 4, 4, 5, 4, 5]


def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    # Не возвращаем результат, а печатаем его
    ic(name + ":", result)


mean_mark("Ivanov", *marks)
# Должно быть напечатано:
# Kuznetsov: 4.454545454545454

print("#" * 40, "**kwargs - keyword arguments", "#" * 40)


# В переменную kwargs будут записаны все
# именованные аргументы
def schedule(**kwargs):
    # kwargs — это словарь, проверим это с помощью isinstance:
    ic(isinstance(kwargs, dict))
    # Напечатаем объект kwargs
    ic(kwargs)


schedule(monday="Python", tuesday="SQL", friday="ML")
# Будет напечатано:
# True
# {'monday': 'Python', 'tuesday': 'SQL', 'friday': 'ML'}

# schedule(monday='Python', tuesday='SQL', 5='ML')
# Будет напечатано:
# SyntaxError: keyword can't be an expression


def schedule(**kwargs):
    print("Week schedule:")
    for key in kwargs:
        print(key, kwargs[key], sep=" - ")


schedule(monday="Python", tuesday="SQL", friday="ML")
# Будет напечатано:
# Week schedule:
# monday — Python
# tuesday — SQL
# friday — ML

lessons = {"Wednesday": "Maths", "Thursday": "SQL", "Friday": "Statistics"}
# Использовали оператор ** для распаковки словаря в набор
# значений именованных аргументов
schedule(**lessons)
# Будет напечатано:
# Week schedule:
# Wednesday — Maths
# Thursday — SQL
# Friday — Statistics
