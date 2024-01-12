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
print(reg)
## [('Petrova', 'Maria', 'Ivanovna', 13, 3, 2003), ('Ivanov', 'Sergej', None, 24, 9, 1995), ('Smith', 'John', None, 13, 2, 2003)]

# reg = register("Ivanov", "Sergej", "24.13.1995")
## ValueError: Invalid Date!
