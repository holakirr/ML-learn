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
