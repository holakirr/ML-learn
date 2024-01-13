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
