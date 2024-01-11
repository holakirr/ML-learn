from icecream import ic

print("#" * 100)
print("Lambda")
print("#" * 100)


def root(num):
    # Напоминание: в Python используется оператор **
    # для возведения числа в степень.
    # В математике возведение в степень ½ соответствует
    # вычислению квадратного корня.
    return num ** (1 / 2)


ic(root(9))

root = lambda num: num ** (1 / 2)
ic(root(9))

print("#" * 40, "Lambda with *args", "#" * 40)

# Для получения корня произвольной степени от числа
# (например, корня степени 4) необходимо возвести исходное
# число в степень, равную единице, делённой на желаемую
# степень корня.
nth_root = lambda num, n: num ** (1 / n)
ic(nth_root(9, 2))

print("#" * 40, "Lambda with condition", "#" * 40)
# Напоминание: оператор % используется для получения остатка
# от деления. Если остаток от деления на 2 равен 0, то
# число является чётным.
# Обратный слэш (\) используется в Python для того,
# чтобы перенести одну строку кода на следующую строку.
# Получается, что компьютер интерпретирует записанное ниже
# как одну строку.
is_even = lambda num: "even" if num % 2 == 0 else "odd"
ic(is_even(4))

print("#" * 40)
func_args = lambda *args: args

ic(func_args(1, 4, 6, 7))
# Будет напечатано:
# (1, 4, 6, 7)

full_func = lambda *args, **kwargs: (args, kwargs)

ic(full_func(1, 5, 6, 7, name="Ivan", age=25))
# Будет напечатано:
# ((1, 5, 6, 7), {'name': 'Ivan', 'age': 25})

print("#" * 40)
names = ["Ivan", "Kim", "German", "Margarita", "Simon"]
names.sort()
ic(names)
# Будет напечатано:
# ['German', 'Ivan', 'Kim', 'Margarita', 'Simon']

names.sort(key=lambda name: len(name))
print(names)
# Будет напечатано:
# ['Kim', 'Ivan', 'Simon', 'German', 'Margarita']


def get_length(name):
    return len(name)


new_list = ["bbb", "ababa", "aaa", "aaaaa", "cc"]
new_list.sort(key=get_length)
ic(new_list)
# Должно быть напечатано:
# ['cc', 'bbb', 'aaa', 'ababa', 'aaaaa']

new_list.sort(key=lambda word: (len(word), word))
ic(new_list)
# Будет напечатано:
# ['cc', 'aaa', 'bbb', 'aaaaa', 'ababa']

print("#" * 40)


def sort_sides(l_in):
    l_in.sort(key=lambda tup: (tup[0] ** 2 + tup[1] ** 2) ** (1 / 2))
    return l_in


ic(sort_sides(l_in=[]))
ic(sort_sides([(3, 4), (1, 2), (10, 10)]))
# [(1, 2), (3, 4), (10, 10)]
