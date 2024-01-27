from hmac import new

from icecream import ic

print("#" * 100)
print(".filter()")
print("#" * 100)

print("#" * 40, "Example 1", "#" * 40)
words_list = [
    "We're",
    "in",
    "a",
    "small",
    "village",
    "near",
    "Chicago",
    "My",
    "cousin's",
    "getting",
    "married.",
]
# res = ['in', 'near', 'My', "cousin's", 'married.']
# Создаём пустой список, куда будем добавлять результаты
even_list = []
# Создаём цикл по элементам списка
for word in words_list:
    # Проверяем условие, что длина текущего слова чётная
    if len(word) % 2 == 0:  # Если условие выполняется
        # Добавляем слово в новый список
        even_list.append(word)
ic(even_list)

## Будет выведено:
## ['in', 'near', 'My', "cousin's", 'married.']

is_even = lambda word: len(word) % 2 == 0

# Применяем функцию is_even() к каждому элементу списка
# Для этого передаём функцию is_even() и список words_list в функцию filter
even = filter(is_even, words_list)
# Смотрим, что получилось
ic(even)

## Будет выведено:
## <filter object at 0x000001758F62D2B0>

# Применяем функцию is_even() к каждому элементу списка
# Для этого передаём функцию is_even() и список words_list в функцию filter
# Результат оборачиваем в список
even_list = list(filter(is_even, words_list))
# Смотрим, что получилось
ic(even_list)

## Будет выведено:
## ['in', 'near', 'My', "cousin's", 'married.']

print("#" * 40, "Example 2", "#" * 40)
str_tuple = ("Москва", "15.1 см", "зацвело", "было пол 5 утра", "рассвет")
# res = ['Москва', 'зацвело', 'рассвет']
ic("Москва".isalpha())
## Будет выведено:
## True

ic("было пол 5 утра".isalpha())
## Будет выведено:
## False

# Применяем lambda-функцию к каждому элементу кортежа
# Результат оборачиваем в кортеж
filtered_tuple = tuple(filter(lambda x: x.isalpha(), str_tuple))
# Смотрим, что получилось
ic(filtered_tuple)
## Будет выведено:
## ('Москва', 'зацвело', 'рассвет')

print("#" * 40, "Example 3", "#" * 40)
data = [
    ("FPW-2.0_D", "Бонус: Тренажер по HTML", 10, 100, 10),
    ("FPW-2.0", "Бонус: Тренажер по JavaScript", 9.2, 70, 180),
    ("FPW-2.0_D", "Бонус: Тренажер по React", 8.5, 66.67, 68),
    ("FPW-2.0", "Бонусный: IT в современном мире", 8.64, 83.74, 856),
    ("FPW-2.0", "Бонусный: Введение", 8.73, 56.24, 745),
    ("FPW-2.0", "Бонус: D1. Знакомство с Django (NEW)", 9.76, 95.24, 21),
    ("FPW-2.0_D", "Бонус: D2. Модели (NEW)", 9.44, 77.78, 18),
]
# Данные по каждому модулю представлены в виде кортежей, состоящих из пяти элементов:
# Кодовое название курса.
# Название курса.
# Средняя оценка модуля.
# NESSA — это внутренняя метрика компании, показывающая качество модуля (измеряется от 0 до 100).
# Количество оценок.

# res = [('FPW-2.0', 'Бонус: Тренажер по JavaScript', 9.2, 70, 180), ('FPW-2.0', 'Бонусный: IT в современном мире', 8.64, 83.74, 856)]


def filter_module(module):
    # Распаковываем кортеж на пять переменных
    code, name, avg_votes, nessa, count = module
    # Создаём условия
    cond_1 = code == "FPW-2.0"
    cond_2 = nessa >= 70
    cond_3 = count > 50
    # Условия должны выполняться одновременно
    return cond_1 and cond_2 and cond_3


ic(filter_module(module=("FPW-2.0_D", "Бонус: Тренажер по HTML", 10, 100, 10)))
## Будет выведено:
## False

ic(filter_module(module=("FPW-2.0", "Бонус: Тренажер по JavaScript", 9.2, 70, 180)))
## Будет выведено:
## True

# Применяем функцию filter_module() для фильтрации списка кортежей
filtered_data = list(filter(filter_module, data))
ic(filtered_data)
## Будет выведено:
## [('FPW-2.0', 'Бонус: Тренажер по JavaScript', 9.2, 70, 180), ('FPW-2.0', 'Бонусный: IT в современном мире', 8.64, 83.74, 856)]

# Создаём lambda-функцию, которая возвращает True, если модуль удовлетворяет условиям
lambda_filter_module = lambda x: (x[0] == "FPW-2.0") and (x[3] >= 70) and (x[4] > 50)
# Применяем эту функцию к каждому элементу списка (к каждому кортежу)
filtered_data = list(filter(lambda_filter_module, data))
# Смотрим, что получилось
ic(filtered_data)
## [('FPW-2.0', 'Бонус: Тренажер по JavaScript', 9.2, 70, 180), ('FPW-2.0', 'Бонусный: IT в современном мире', 8.64, 83.74, 856)]

print("#" * 40, "Task 1", "#" * 40)
prices = [34562, 66572, 25683, 17683, 56389, 28973]
## filtered_prices = [25683, 17683, 28973]
filtered_prices = list(filter(lambda x: x < 30000, prices))
ic(filtered_prices)

print("#" * 40, "Task 2", "#" * 40)
family_list = [
    "certificate of a large family",
    "social card",
    "maternity capital",
    "parking permit",
    "tax benefit",
    "reimbursement of expenses",
    "compensation for the purchase of children's goods",
]
filter_family = lambda lst: list(filter(lambda x: x in family_list, lst))
ic(
    filter_family(
        [
            "newborn registration",
            "parking permit",
            "maternity capital",
            "tax benefit",
            "medical policy",
        ]
    )
)
## ['parking permit', 'maternity capital', 'tax benefit']

print("#" * 40, "Example 4", "#" * 40)
# Список из слов
words_list = [
    "We're",
    "in",
    "a",
    "small",
    "village",
    "near",
    "Chicago",
    "My",
    "cousin's",
    "getting",
    "married.",
]
# res = [("We're", 0), ('small', 1), ('village', 1), ('Chicago', 1), ("cousin's", 0), ('getting', 0), ('married.', 1)]
# Создаём пустой список, в который будем добавлять результаты
count_a = []
# Создаём цикл по элементам списка words_list
for word in words_list:
    # Проверяем условие, что длина имени больше либо равна пяти
    if len(word) >= 5:
        # Создаём кортеж (слово, количество букв 'a')
        result_tuple = (word, word.lower().count("a"))
        # Добавляем в итоговый список кортеж
        count_a.append(result_tuple)
ic(count_a)

## Будет выведено:
## [("We're", 0), ('small', 1), ('village', 1), ('Chicago', 1), ("cousin's", 0), ('getting', 0), ('married.', 1)]

# Отбираем слова из пяти и более букв
filtered_words = filter(lambda x: len(x) >= 5, words_list)
ic(filtered_words)
# Все отобранные слова переводим в нижний регистр и считаем число букв 'a' в них
# Результат выдаём в виде кортежа (слово, количество букв "a")
count_a = map(lambda x: (x, x.lower().count("a")), filtered_words)
ic(count_a)
# Переводим объект map в list и печатаем его
ic(list(count_a))

## Будет выведено:
## [("We're", 0), ('small', 1), ('village', 1), ('Chicago', 1), ("cousin's", 0), ('getting', 0), ('married.', 1)]

print("#" * 40, "Example 5", "#" * 40)
# Выгрузка данных о параметрах человеческого тела
data = [
    ("Amanda", 1.61, 51),
    ("Patricia", 1.65, 61),
    ("Marcos", 1.91, 101),
    ("Andrey", 1.79, 61),
    ("Nikos", 1.57, 78),
    ("Felicia", 1.63, 56),
    ("Lubov", 1.53, 34),
]
# Решение
# Создаём lambda-функцию, которая считает BMI, и применяем её к каждому элементу списка
map_func = lambda x: (*x, x[2] / (x[1] ** 2))
updated_data = map(map_func, data)

# Итоговый код
# Создаём lambda-функцию, которая считает BMI, и применяем её к каждому элементу списка
map_func = lambda x: (*x, x[2] / (x[1] ** 2))
updated_data = map(map_func, data)
# Создаём lambda-функцию, которая возвращает True, если 18.5 <= BMI <= 25
filter_func = lambda x: 18.5 <= x[3] <= 25
# Применяем эту функцию к результату работы map()
filtered_data = filter(filter_func, updated_data)
# Переводим объект filter в list и печатаем его
ic(list(filtered_data))

## Будет выведено:
## [('Amanda', 1.61, 51, 19.7), ('Patricia', 1.65, 61, 22.4), ('Andrey', 1.79, 61, 19.0), ('Felicia', 1.63, 56, 21.1)]

print("#" * 40, "Task 3", "#" * 40)
reg = [
    ("Ivanov", "Sergej", 24, 9, 1995),
    ("Smith", "John", 13, 2, 2003),
    ("Petrova", "Maria", 13, 3, 2003),
]
# new_reg = [('Smith J.', 13, 2, 2003), ('Petrova M.', 13, 3, 2003)]
new_reg = list(
    map(
        lambda x: (f"{x[0]} {x[1][0]}.", *x[2:]),
        list(filter(lambda x: x[4] >= 2000, reg)),
    )
)
ic(new_reg)

print("#" * 40, "Task 4", "#" * 40)
data = [
    (0.00632, 6.575, 65.2, 296.0, 4.98),
    (0.02731, 6.421, 78.9, 242.0, 9.14),
    (0.02729, 7.185, 61.1, 242.0, 4.03),
    (0.03237, 6.998, 45.8, 222.0, 2.94),
    (0.06905, 7.147, 54.2, 222.0, 5.33),
    (0.02985, 6.43, 58.7, 222.0, 5.21),
    (0.08829, 6.012, 66.6, 311.0, 12.43),
]
# filtered_data = [
#     (0.02731, 6.421, 78.9, 242.0, 9.14, 60.41),
#     (0.06905, 7.147, 54.2, 222.0, 5.33, 81.7),
#     (0.08829, 6.012, 66.6, 311.0, 12.43, 341.31),
# ]
filtered_data = list(
    filter(lambda x: x[5] > 60, map(lambda x: (*x, round(x[0] * x[3] * x[4], 2)), data))
)
ic(filtered_data)
