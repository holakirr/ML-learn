from icecream import ic

print("#" * 100)
print("Changing variables out of scope")
print("#" * 100)
ic(dir(__builtins__))
## Будет выведено:

# Объявляем глобальную переменную
count = 10


def func():
    # Объявляем локальную переменную count
    count = 100


# Вызываем функцию
func()
# Смотрим, изменилась ли переменная count
ic(count)

## Будет выведено:
## 10

print("#" * 40)
# Объявляем глобальную переменную
words_list = ["foo", "bar", "baz"]


def funct():
    # Изменяем элемент списка
    words_list[1] = "quux"


# Вызываем функцию
funct()
ic(words_list)

## Будет выведено:
## ['foo', 'quux', 'baz']

print("#" * 40)
# Объявляем глобальную переменную
words_list = ["foo", "bar", "baz"]


def function():
    # Изменяем элемент списка
    words_list = ["foo", "quux", "baz"]


# Вызываем функцию
function()
ic(words_list)

## Будет выведено:
## ['foo', 'bar', 'baz']

print("#" * 40, "Changing variables out of scope. Using Global.", "#" * 40)
# Создадим глобальную переменную, изначально она равна 0
# global_count = 0


# # Создадим функцию, которая прибавляет 1 к переменной global_count
# def add_item():
#     # Здесь мог бы быть код для добавления товара в базу данных
#     # Увеличим общее количество товаров на 1
#     global_count = global_count + 1


# Вызовем функцию add_item()
# add_item()
# Напечатаем значение переменной global_count
# ic(global_count)

## Возникнет ошибка:
## UnboundLocalError: local variable 'global_count' referenced before assignment

print("#" * 40)
# Создадим глобальную переменную, изначально она равна 0
# global_count = 0


# # Создадим функцию, которая прибавляет 1 к переменной global_count
# def add_item():
#     # Здесь мог бы быть код для добавления товара в базу данных

#     # Укажем, что global_count является глобальной переменной
#     global global_count
#     # Увеличим общее количество товаров на 1
#     global_count = global_count + 1


# # Вызовем функцию add_item()
# add_item()
# # Напечатаем значение переменной global_count
# print(global_count)


## Будет выведено:
## 1

print("#" * 40)


# Создаём функцию, которая прибавляет 1 к переменной global_count
def add_item():
    # Здесь мог бы быть код для добавления товара в базу данных
    # Указываем, что global_count является глобальной переменной
    global global_count
    # Инициализируем глобальную переменную прямо внутри функции
    global_count = 0
    # Увеличиваем общее количество товаров на 1
    global_count = global_count + 1


# Вызываем функцию add_item()
add_item()
# Напечатаем значение переменной global_count
print(global_count)


## Будет выведено:
## 1

print("#" * 40)
## Введите свое решение ниже


def cash(less_money):
    global money
    money -= less_money
    return money


money = 200000
ic(cash(1000))

print("#" * 40)
# Словарь с курсами валют (по отношению к рублю)
currencies = {"USD": 74, "EUR": 88, "GBP": 98, "CHF": 82}
# Общее количество денег на счету, которое нужно конвертировать
money = 100000


# Функция для конвертации валюты, аргумент - наименование валюты
def convert(currencies, money, currency):
    # Производим конвертацию - делим количество денег на счету на соответствующий курс
    return money / currencies[currency]


# Вызываем функцию для конвертации валюты
convert_money = convert(currencies, money, "USD")
print(convert_money)

## 1351.3513513513512

print("#" * 40, "Changing variables out of scope. Using nonlocal.", "#" * 40)


# Внешняя функция
# def outer():
#     # Создадим переменную, относящуюся к внешней функции
#     enclosing_count = 0

#     # Внутренняя функция
#     def inner():
#         # Прибавим 1 к enclosing_count
#         enclosing_count = enclosing_count + 1
#         # Напечатаем значение enclosing_count
#         print(enclosing_count)

#     # Запустим внутреннюю функцию из внешней
#     inner()


# Запустим внешнюю функцию
# outer()

# Возникнет ошибка:
# UnboundLocalError: local variable 'enclosing_count' referenced before assignment

print("#" * 40)


# Внешняя функция
def outer():
    # Создадим переменную, относящуюся к внешней функции
    enclosing_count = 0

    # Внутренняя функция
    def inner():
        # Укажем, что используем нелокальную переменную enclosing_count
        nonlocal enclosing_count
        # Прибавим 1 к enclosing_count
        enclosing_count = enclosing_count + 1
        # Напечатаем значение enclosing_count
        print(enclosing_count)

    # Запустим внутреннюю функцию из внешней
    inner()


# Запустим внешнюю функцию
outer()

## Будет напечатано:
## 1

print("#" * 40)


# Внешняя функция для вычисления итоговой стоимости
def calculate_cost(cost, sale):
    # Внутренняя функция для предобработки аргумента sale
    def preprocessing_sale():
        # Объявляем, что используем нелокальную переменную sale
        nonlocal sale
        # Если sale — строка
        if type(sale) is str:
            # Удаляем из строки '%', приводим к float и делим на 100
            sale = float(sale.replace("%", "")) / 100
        # Если sale — целое число
        elif type(sale) is int:
            # Делим его на 100
            sale = sale / 100
        elif type(sale) is not float:
            raise ValueError("Некорректный формат скидки")

    # Запускаем предобработку, прежде чем вычислить стоимость
    preprocessing_sale()
    # Считаем итоговую стоимость и возвращаем её
    # (стоимость — стоимость * скидка)
    return cost - cost * sale


ic(calculate_cost(1000, 10))
ic(calculate_cost(1000, "10%"))
ic(calculate_cost(1000, 0.1))

print("#" * 40)


## Введите свое решение ниже
# Функция для вычисления количества символов (symbol) в строке s
def count_occurrences(s, symbol):
    # Внутренняя функция для предобработки строки s
    def preprocessing_s():
        # Удаляем пробелы из строки
        nonlocal s
        s = s.replace(" ", "")
        # Приводим строку к нижнему регистру
        s = s.lower()

    # Вызываем функцию для предобработки аргумента s
    preprocessing_s()
    # Считаем количество символов symbol в строке s и возвращаем результат
    return s.count(symbol)


ic(count_occurrences("This is simple string", symbol="t"))
## 2

print("#" * 40, "Changing built-in variables.", "#" * 40)
my_list = [1, 4, 5, 7]
# Запишем в переменную с названием
# len длину списка my_list,
# полученную с помощью встроенной функции len
len = len(my_list)
ic(len)


## Будет выведено:
## 4

# Попробуем снова воспользоваться функцией len:
# Создадим ещё один список
new_list = ["Ivan", "Sergej", "Maria"]
# Также узнаем его длину с помощью функции len
# length = len(new_list)
# print(length)
## Возникнет ошибка:
## TypeError: 'int' object is not callable

print("#" * 40)
advertising_campaigns = {"ютуб": [212, 248], "вк": [514, 342], "радио": [339, 125]}
# Создаём новый пустой словарь
advertising_campaigns_max = {}
# Создаём цикл по ключам исходного словаря
for key in advertising_campaigns:
    # Вычисляем максимум в списке, лежащем по ключу key
    maximum = max(advertising_campaigns[key])
    # Добавляем максимум в новый словарь
    advertising_campaigns_max[key] = maximum
ic(advertising_campaigns_max)
