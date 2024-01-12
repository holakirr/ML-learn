from icecream import ic

print("#" * 100)
print("Practice")
print("#" * 100)

inner_counter = 0


def outer_function(value, x):
    global_counter = value

    def inner_function(x):
        global inner_counter
        nonlocal global_counter
        inner_counter += 1
        global_counter += 1
        result = x + inner_counter + global_counter
        return result

    return inner_function(x)


local_result = outer_function(value=3, x=4)

print("#" * 40)


# Внешняя функция для обработки списка из строк
def processing_list(answers):
    # Внутренняя функция для выполнения обработки одного элемента списка
    def preprocessing_answer(answer):
        # Приводим к нижнему регистру
        answer = answer.lower()
        # Удаляем стоп-символы
        stop_symbols = "\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~!"
        # Создаём цикл по символам в строке
        for sym in stop_symbols:
            # Если стоп-символ есть в строке answer
            if sym in answer:
                # Заменяем стоп-символы в строке на пустые строки
                answer = answer.replace(sym, "")
        return answer

    # Создаём пустой список, куда будем добавлять результаты
    result = []
    # Создаеё цикл по всем элементам списка
    for answer in answers:
        # Добавляем предобработанную строку в лог-список
        result.append(preprocessing_answer(answer))
    return result


print("#" * 40)


# Функция для регистрации пользователей
def register(surname, name, date, middle_name=None, registry=None):
    # Вспомогательная функция для предобработки даты
    def preprocessing_date(date):
        # Функция для проверки корректности даты
        def check_date(day, month, year):
            # Проверяем день, месяц и год на целочисленность
            if (
                (type(day) is not int)
                or (type(month) is not int)
                or (type(year) is not int)
            ):
                return False
            # Проверяем год на заданный диапазон
            if (year <= 1900) or (year >= 2022):
                return False
            # Проверяем месяц на заданный диапазон
            if (month < 1) or (month > 12):
                return False
            # Проверяем день на заданный диапазон
            if (day < 1) or (day > 31):
                return False
            # Проверяем апрель, июнь, сентябрь и ноябрь на количество дней
            if (month in [4, 6, 9, 11]) and (day > 30):
                return False
            # Проверяем количество дней в феврале
            if month == 2 and day > 28:
                return False
            return True

        # Разделяем строку по символу точки
        day, month, year = date.split(".")
        # Преобразуем все данные к типу данных int
        day, month, year = int(day), int(month), int(year)
        return day, month, year

    # Если список не был передан — создаём пустой список
    if registry is None:
        registry = list()
    # Разделяем дату на составляющие
    day, month, year = preprocessing_date(date)
    # Добавляем данные в список
    registry.append((surname, name, middle_name, day, month, year))
    return registry


reg = register("Petrova", "Maria", "13.03.2003", "Ivanovna")

reg = register("Ivanov", "Sergej", "24.09.1995", registry=reg)

reg = register("Smith", "John", "13.02.2003", registry=reg)
ic(reg)
## [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]

print("#" * 40)


# Введите свое решение ниже
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


ic(is_leap(2000))
# True
ic(is_leap(1900))
# False
ic(is_leap(2020))
# True
ic(is_leap(1700))
# False

print("#" * 40)


# Функция для проверки корректности даты
def check_date(day, month, year):
    # Введите свое решение ниже
    def is_leap(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    # Проверяем день, месяц и год на целочисленность
    if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
        return False
    # Проверяем год на заданный диапазон
    if (year <= 1900) or (year >= 2022):
        return False
    # Проверяем месяц на заданный диапазон
    if (month < 1) or (month > 12):
        return False
    # Проверяем день на заданный диапазон
    if (day < 1) or (day > 31):
        return False
    # Проверяем апрель, июнь, сентябрь и ноябрь на количество дней
    if (month in [4, 6, 9, 11]) and (day > 30):
        return False
    # Проверяем количество дней в феврале
    if month == 2:
        if is_leap(year) and day > 29:
            return False
        if not is_leap(year) and day > 28:
            return False
    return True


ic(check_date(18, 9, 1999))
# True
ic(check_date(29, 2, 2000))
# True
ic(check_date(29, 2, 2021))
# False
ic(check_date(13, 13, 2021))
# False
ic(check_date(13.5, 12, 2021))
# False

print("#" * 40)


# Нам остался финальный штрих — добавить проверку даты на корректность в функцию для регистрации!
def register(surname, name, date, middle_name=None, registry=None):
    # Вспомогательная функция для предобработки даты
    def preprocessing_date(date):
        # Разделяем строку по символу точки
        day, month, year = date.split(".")
        # Преобразуем все данные к типу данных int
        day, month, year = int(day), int(month), int(year)
        return day, month, year

    day, month, year = preprocessing_date(date)

    # Функция для проверки корректности даты
    def check_date(day, month, year):
        # Проверяем день, месяц и год на целочисленность
        if (
            (type(day) is not int)
            or (type(month) is not int)
            or (type(year) is not int)
        ):
            return False
        # Проверяем год на заданный диапазон
        if (year <= 1900) or (year >= 2022):
            return False
        # Проверяем месяц на заданный диапазон
        if (month < 1) or (month > 12):
            return False
        # Проверяем день на заданный диапазон
        if (day < 1) or (day > 31):
            return False
        # Проверяем апрель, июнь, сентябрь и ноябрь на количество дней
        if (month in [4, 6, 9, 11]) and (day > 30):
            return False
        # Проверяем количество дней в феврале
        if month == 2 and day > 28:
            return False
        return True

    if not check_date(day, month, year):
        raise ValueError("Invalid Date!")

    # Если список не был передан — создаём пустой список
    if registry is None:
        registry = list()
    # Разделяем дату на составляющие
    day, month, year = preprocessing_date(date)
    # Добавляем данные в список
    registry.append((surname, name, middle_name, day, month, year))
    return registry


reg = register("Petrova", "Maria", "13.03.2003", "Ivanovna")
reg = register("Ivanov", "Sergej", "24.09.1995", registry=reg)
reg = register("Smith", "John", "13.02.2003", registry=reg)
ic(reg)
## [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]

# reg = register("Ivanov", "Sergej", "24.13.1995")
## ValueError: Invalid Date!

print("#" * 40, "Second task", "#" * 40)

Point = tuple[int, int]


# Функция для вычисления сторон треугольника
def sides(p1: Point, p2: Point, p3: Point):
    # Распаковываем кортежи для удобства
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Вычисляем стороны по теореме Пифагора
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    return a, b, c


ic(sides(p1=(2, 2), p2=(4, 1.25), p3=(1, 4.5)))
## (2.1360009363293826, 2.692582403567252, 4.422951503238533)
ic(sides(p1=(1, 1), p2=(1, 4), p3=(5, 1)))
## (3.0, 4.0, 5.0)


# Функция для вычисления периметра треугольника
def calculate_perimeter_triangle(a, b, c):
    # Периметр — сумма всех сторон треугольника
    perimeter = a + b + c
    return perimeter


# Функция для вычисления площади треугольника
def calculate_area_triangle(a, b, c):
    # Вычисляем полупериметр
    half_p = calculate_perimeter_triangle(a, b, c) / 2
    # Вычисляем площадь по формуле Герона
    area = (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5
    return area


ic(calculate_perimeter_triangle(a=3, b=4, c=5))
ic(calculate_area_triangle(a=3, b=4, c=5))
## 12
## 6.0

print("#" * 40)


def triangle(p1, p2, p3):
    # Функция для вычисления сторон треугольника
    # По умолчанию параметры функции берутся из объемлющей области видимости
    def sides(p1, p2, p3):
        # Распаковываем кортежи для удобства, “;” означает новую строку кода
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        # Вычисляем стороны по теореме Пифагора
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        return a, b, c

    # Функция для вычисления периметра треугольника
    def calculate_perimeter_triangle(a, b, c):
        # Периметр — сумма всех сторон треугольника
        perimeter = a + b + c
        return perimeter

    # Функция для вычисления площади треугольника
    def calculate_area_triangle(a, b, c):
        # Вычисляем полупериметр
        # Значение perimeter берётся из объемлющей области видимости
        p = perimeter / 2
        # Вычисляем площадь по формуле Герона
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area

    a, b, c = sides(p1, p2, p3)
    perimeter = calculate_perimeter_triangle(a, b, c)
    area = calculate_area_triangle(a, b, c)
    result = {"a": a, "b": b, "c": c, "perimeter": perimeter, "area": area}
    return result


ic(triangle(p1=(2, 2), p2=(4, 1.25), p3=(1, 4.5)))
## {'a': 2.1360009363293826, 'b': 2.692582403567252, 'c': 4.422951503238533, 'perimeter': 9.251534843135168, 'area': 2.1250000000000027}
ic(triangle(p1=(1, 1), p2=(1, 4), p3=(5, 1)))
## {'a': 3.0, 'b': 4.0, 'c': 5.0, 'perimeter': 12.0, 'area': 6.0}

print("#" * 40)
# Из математики известно, что треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.


def check_exist_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


ic(check_exist_triangle(a=3, b=4, c=5))
## True
ic(check_exist_triangle(a=1.8, b=1.8, c=3.6))
## False

print("#" * 40)
# Now I'd love to make it lambda function

check_exist_triangle = lambda a, b, c: a + b > c and a + c > b and b + c > a


ic(check_exist_triangle(a=3, b=4, c=5))
## True
ic(check_exist_triangle(a=1.8, b=1.8, c=3.6))
## False

print("#" * 40)
# And now let's combine it all together


def triangle(p1, p2, p3):
    check_exist_triangle = lambda a, b, c: a + b > c and a + c > b and b + c > a

    # Функция для вычисления сторон треугольника
    # По умолчанию параметры функции берутся из объемлющей области видимости
    def sides(p1, p2, p3):
        # Распаковываем кортежи для удобства, “;” означает новую строку кода
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        # Вычисляем стороны по теореме Пифагора
        a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        return a, b, c

    # Функция для вычисления периметра треугольника
    def calculate_perimeter_triangle(a, b, c):
        # Периметр — сумма всех сторон треугольника
        perimeter = a + b + c
        return perimeter

    # Функция для вычисления площади треугольника
    def calculate_area_triangle(a, b, c):
        # Вычисляем полупериметр
        # Значение perimeter берётся из объемлющей области видимости
        p = perimeter / 2
        # Вычисляем площадь по формуле Герона
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area

    a, b, c = sides(p1, p2, p3)
    if not check_exist_triangle(a, b, c):
        raise ValueError("Треугольник не существует")
    perimeter = calculate_perimeter_triangle(a, b, c)
    area = calculate_area_triangle(a, b, c)
    result = {"a": a, "b": b, "c": c, "perimeter": perimeter, "area": area}
    return result


print(triangle(p1=(2, 2), p2=(4, 1.25), p3=(1, 4.5)))
## {'a': 2.1360009363293826, 'b': 2.692582403567252, 'c': 4.422951503238533, 'perimeter': 9.251534843135168, 'area': 2.1250000000000027}
print(triangle(p1=(1, 1), p2=(1, 4), p3=(5, 1)))
## {'a': 3.0, 'b': 4.0, 'c': 5.0, 'perimeter': 12.0, 'area': 6.0}
# print(triangle(p1=(2.5, 2), p2=(4, 1), p3=(1, 3)))
## ValueError: Треугольник не существует

print("#" * 40, "Third task", "#" * 40)
# Now it's about a circle
p1, p2 = (3, 2.5), (4, 4.5)


radius = lambda p1, p2: ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

print("#" * 40)


def circle(p1, p2):
    radius = lambda p1, p2: ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    calculate_circumference = lambda radius: 2 * pi * radius
    calculate_area_circle = lambda radius: pi * radius**2
    return {
        "radius": round(radius(p1, p2), 3),
        "circumference": round(calculate_circumference(radius(p1, p2)), 3),
        "area": round(calculate_area_circle(radius(p1, p2)), 3),
    }


pi = 3.1416
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.05, 'area': 15.708}

pi = 3.1416
print(circle(p1=(0, 0), p2=(1, 1)))
## {'radius': 1.414, 'circumference': 8.886, 'area': 6.283}

pi = 3.14
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.043, 'area': 15.7}

print("#" * 40, "Fourth task", "#" * 40)
# Now it's about an ellipse


# p1 - center of ellipse
def semi_axes(p1: Point, p2: Point, p3: Point):
    a = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    b = ((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2) ** 0.5
    return a, b


ic(semi_axes(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5)))
## (1.5, 1.0)

# Let's make it lambda function
semi_axes = lambda p1, p2, p3: (
    (((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5),
    (((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2) ** 0.5),
)

ic(semi_axes(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5)))
## (1.5, 1.0)

print("#" * 40)


def ellipse(p1, p2, p3):
    semi_axes = lambda p1, p2, p3: (
        (((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5),
        (((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2) ** 0.5),
    )
    calculate_circumference = lambda a, b: 2 * pi * ((a**2 + b**2) / 2) ** 0.5
    calculate_area_ellipse = lambda a, b: pi * a * b
    a, b = semi_axes(p1, p2, p3)
    return {
        "a": round(a, 3),
        "b": round(b, 3),
        "length": round(calculate_circumference(a, b), 3),
        "area": round(calculate_area_ellipse(a, b), 3),
    }


pi = 3.1416
ic(ellipse(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5)))

## {'a': 1.5, 'b': 1.0, 'length': 8.01, 'area': 4.712}

pi = 3.1416
ic(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))

## {'a': 1.0, 'b': 1.0, 'length': 6.283, 'area': 3.142}

pi = 3.14
ic(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))
## {'a': 1.0, 'b': 1.0, 'length': 6.28, 'area': 3.14}
