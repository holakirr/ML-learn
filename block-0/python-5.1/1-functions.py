from icecream import ic

print("#" * 40, "Functions", "#" * 40)


def first_function():
    ic("Hello world!")


first_function()


def print_hours(minutes):
    # // — это оператор целочисленного деления
    hours = minutes // 60
    # % — это оператор получения остатка от деления
    left_minutes = minutes % 60
    print("Hours:", hours)
    print("Minutes left:", left_minutes)


print_hours(90)
# Будет напечатано:
# Hours: 1
# Minutes left: 30

print("#" * 40, "Return", "#" * 40)


# Назовём функцию get_time (get — получать,
# time — время). Она принимает аргументы
# distance — расстояние и speed — скорость.
def get_time(distance, speed):
    # В переменную result сохраним результат
    # деления расстояния на скорость.
    result = distance / speed

    # Чтобы вернуть результат вычислений,
    # пишем оператор return и название переменной,
    # значение которой будет передано.
    return result


# В переменную time сохранится результат вычисления
# времени в пути длиной 120 км при скорости 60 км/ч.
time = int(get_time(120, 60))
ic(time)


print("#" * 40, "Multiple return", "#" * 40)


def get_time_tuple(distance: int, speed: int):
    # Получаем целое число часов в пути
    hours = distance // speed
    # Получаем остаток км в пути
    distance_left = distance % speed
    # Переводим скорость из км/ч в км/мин:
    # за одну минуту можно проехать расстояние
    # в 60 раз меньше, чем за 1 час
    kms_per_minute = speed / 60
    # Делим оставшееся расстояние на скорость в км/мин.
    # и округляем до целого
    minutes = round(distance_left / kms_per_minute)

    # Перечисляем аргументы через запятую.
    # Они будут возвращены функцией в виде кортежа.
    return hours, minutes


result = get_time_tuple(120, 100)
ic(result)
# Будет напечатано:
# (1, 12)

# Нулевой элемент кортежа — часы
# Первый элемент —  минуты
ic("Hours to travel:", result[0])
ic("Minutes to travel:", result[1])
# Будет напечатано:
# Hours to travel: 1
# Minutes to travel: 12

# Через запятую перечисляем переменные, в которые сохранится результат
hours, minutes = get_time_tuple(120, 100)
# Красиво напечатаем результат
ic("Hours to travel:", hours)
ic("Minutes to travel:", minutes)
# Будет напечатано:
# Hours to travel: 1
# Minutes to travel: 12

print("#" * 40)


# list_in — список, в котором будем искать объект
# Интуитивно хотелось бы назвать аргумент для списка
# словом list, однако это привело бы к изменению встроенного
# объекта list, что очень нежелательно
# obj — аргумент, содержащий объект, который ищет функция
def in_list(list_in, obj):
    for elem in list_in:
        if obj == elem:
            ic("Element is found!")
            return True
            ic("This won’t be iced")
    ic("Element is NOT found!")
    return False
    ic("This will not be iced either")


my_list = [1, 2, 5, 7, 10]
result = in_list(my_list, 3)
# Element is NOT found!
ic(result)
# False
result = in_list(my_list, 7)
# Element is found!
ic(result)
# True
