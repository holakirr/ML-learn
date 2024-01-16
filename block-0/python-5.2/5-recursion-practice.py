from icecream import ic

print("#" * 100)
print("Recursion practice")
print("#" * 100)


## Введите свое решение ниже
def power(val, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(val, -n)
    return val * power(val, n - 1)


ic(power(25, 0))
# 1
ic(power(-5, 4))
# 625

print("#" * 40)


# Функция для создания строки со скобками
def add_brackets(s):
    # Проверяем условие остановки: строка состоит из одного или двух символов
    if len(s) == 1 or len(s) == 2:
        # Возвращаем эти символы
        return s
    # В противном случае:
    # «Отщипываем» от строки первый и последний символы,
    # добавляем к ним скобки, а также результат вызова функции, в которую
    # передаем строку без первого и последнего символов
    return s[0] + "(" + add_brackets(s[1:-1]) + ")" + s[-1]


ic(add_brackets("example"))
ic(add_brackets("carr"))
ic(add_brackets("hello"))

## Будет выведено:
## e(x(a(m)p)l)e
## c(ar)r
## h(e(l)l)o


# With cycle
# def add_brackets(s):
#     # Вычисляем середину строки
#     l = len(s) // 2
#     # Если длина строки чётная
#     if len(s) % 2 == 0:
#         # В список исключений добавляются индексы l-1 и l
#         for_exclude = [l - 1, l]
#     else:  # Если нечётная
#         # В список исключений добавляется индекс l
#         for_exclude = [l]
#     # Создаём пустую строку
#     result = ""
#     # Создаём цикл по индексам строки
#     for i in range(len(s)):
#         # Если номер символа — в списке исключений, добавляем символ
#         if i in for_exclude:
#             result += s[i]
#         # Если номер символа меньше середины, добавляем символ и левую скобку
#         elif i < l:
#             result += s[i] + "("
#         # Если мы перешли за середину строки, добавляем символ и правую скобку
#         else:
#             result += ")" + s[i]
#     # Возвращаем результат
#     return result


print("#" * 40)


def add_asterisk(s):
    if len(s) == 1:
        return s
    return s[0] + "*" + add_asterisk(s[1:])


print(add_asterisk("hello"))
## h*e*l*l*o
print(add_asterisk("LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO"))
## L*I*t*B*e*o*F*L*c*S*G*B*O*F*Q*x*M*H*o*I*u*D*D*W*c*q*c*V*g*k*c*R*o*A*e*o*c*X*O
print(add_asterisk("gkafkafkKdaflkfa"))
## g*k*a*f*k*a*f*k*K*d*a*f*l*k*f*a

print("#" * 40)
matrix = [[1, 1, 0], [4, 2, 1], [0, 2, 1]]


# Функция для выпрямления списка
def flatten(lst):
    # Создаём новый пустой список
    result = []
    # Создаём цикл по элементам списка
    for elem in lst:
        # Если элемент списка является списком,
        if type(elem) is list:
            # Применяем к нему функцию выпрямления и добавляем элементы к результату
            result += flatten(elem)
        else:  # Если элемент не является списоком,
            # Добавляем элемент в новый список
            result.append(elem)
    return result


ic(flatten(matrix))


## Будет выведено:
## [1, 1, 0, 4, 2, 1, 0, 2, 1]
matrix = [[1, 1, [5, 10, 34, [24, 1, 0]]], [4, [9, 8, 10], 1], [0, 2, 1]]
ic(flatten(matrix))


## Будет выведено:
## [1, 1, 5, 10, 34, 24, 1, 0, 4, 9, 8, 10, 1, 0, 2, 1]

print("#" * 40)
matrix = [[1, 1, 0], [4, 2, 1], [0, 2, 1]]


def sum_list(matrix):
    if not matrix:
        return 0
    if type(matrix[0]) is list:
        return sum_list(matrix[0]) + sum_list(matrix[1:])
    return matrix[0] + sum_list(matrix[1:])


ic(sum_list(matrix))
## 12
matrix = [[1, 1, [1, 2, 3], 0], [4, 2, 1, [10, 52, 2]], [0, 2, 1]]
ic(sum_list(matrix))
## 82

print("#" * 40)
forum_messages = {
    1: {"parent_link": None, "child_link": [3, 4]},
    2: {"parent_link": None, "child_link": [5]},
    3: {"parent_link": 1, "child_link": [6]},
    4: {"parent_link": 1, "child_link": []},
    5: {"parent_link": 2, "child_link": []},
    6: {"parent_link": 3, "child_link": []},
}


# Функция для удаления сообщения на форуме и всех его потомков
def delete_message(messages, msg_id):
    # Удаляем из словаря сообщение с идентификатором msg_id
    # Метод pop() возвращает значение, лежащее по удаляемому ключу
    result = messages.pop(msg_id)
    # Получаем идентификатор родителя
    parent_link = result["parent_link"]
    # Получаем список идентификаторов потомков
    child_link = result["child_link"]
    # Если у сообщения был родитель и он ещё не был удален
    # Эта запись будет аналогична parent_link is not None
    if parent_link and parent_link in messages:
        # Обращаемся к словарю messages по ключу родителя
        # Удаляем потомка из списка потомков
        messages[parent_link]["child_link"].remove(msg_id)
    # Если у сообщения были потомки
    # Эта запись будет аналогична child_link == []
    if child_link:
        # В цикле проходимся по всем потомкам
        for child_id in child_link:
            # И повторяем те же самые действия для каждого из них
            # (рекурсивно вызываем функцию delete_message)
            delete_message(messages, msg_id=child_id)
    return messages


ic(delete_message(forum_messages, msg_id=5))
## Будет выведено:
## {1: {'parent_link': None, 'child_link': [3, 4]}, 2: {'parent_link': None, 'child_link': []}, 3: {'parent_link': 1, 'child_link': [6]}, 4: {'parent_link': 1, 'child_link': []}, 6: {'parent_link': 3, 'child_link': []}}
ic(delete_message(forum_messages, msg_id=3))
## Будет выведено:
## {1: {'parent_link': None, 'child_link': [4]}, 2: {'parent_link': None, 'child_link': [5]}, 4: {'parent_link': 1, 'child_link': []}, 5: {'parent_link': 2, 'child_link': []}}
ic(delete_message(forum_messages, msg_id=1))
## Будет выведено:
## {2: {'parent_link': None, 'child_link': [5]}, 5: {'parent_link': 2, 'child_link': []}}

print("#" * 40)
input_dict = {
    "key1": {"key2": ["value1", "value2"], "key3": {"key4": ["value3"]}},
    "key5": {"key6": {"key7": ["value3", "value5", "value6"]}},
}


def print_dict(input_data, level=0):
    # Если input_data — словарь
    if type(input_data) is dict:
        # Создаём цикл по ключам словаря
        for key in input_data:
            # Выводим ключ в формате "<пробелы> <имя ключа> ->"
            print("  " * level + "{} ->".format(key))
            # Повторяем те же операции для каждого значения словаря
            print_dict(input_data[key], level=level + 1)
    else:  # В противном случае
        # Выводим значения в формате "<пробелы> <значения>"
        print("  " * level + str(input_data))


print_dict(input_dict)
# key1 ->
#   key2 ->
#     ['value1', 'value2']
#   key3 ->
#     key4 ->
#       ['value3']
# key5 ->
#   key6 ->
#     key7 ->
#       ['value3', 'value5', 'value6']
