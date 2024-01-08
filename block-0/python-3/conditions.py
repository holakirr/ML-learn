from icecream import ic

print("#" * 100)
print("Conditions")
print("#" * 100)

print("#" * 40, "Comparison of numbers", "#" * 40)
# Создаём 3 переменные, в которых содержится прибыль за 3 года
income_2019 = 15
income_2020 = 16.5
income_2021 = 16.5
# Проверяем равенство прибылей за 2019 и 2020 год
ic(income_2019 == income_2020)
# False
# Проверяем равенство прибылей за 2020 и 2021 год
ic(income_2020 == income_2021)
# True
print("#" * 40)
# Проверяем, что прибыль за 2019 год больше либо равна прибыли за 2020
ic(income_2019 >= income_2020)
# False
# Проверяем, что прибыль за 2020 год больше либо равна прибыли за 2021
ic(income_2020 >= income_2021)
# True

print("#" * 40, "Comparison of strings", "#" * 40)
# Создаём 3 переменных с именами пользователей
name_user_1029 = "Andrey"
name_user_1040 = "Vladimir"
name_user_1042 = "Andrey"
# Сравниваем имена пользователей друг с другом
ic(name_user_1029 == name_user_1040)
# False
ic(name_user_1040 == name_user_1042)
# True

print("#" * 40)
ic(ord("A"))
# 65
ic(ord("a"))
# 97

print("#" * 40)
# Создаём строку в нижнем регистре
string_lower = "test string"
# Создаём строку в верхнем регистре
string_upper = "TEST STRING"
# Проверяем их равенство
ic(string_lower == string_upper)
# False

print("#" * 40)
# Создаём строку
string_without_space = "test string"
# Создаём ту же строку, но пробелом в конце
string_with_space = "test string "
# Проверяем их равенство
ic(string_with_space == string_without_space)
# False

print("#" * 40, "Comparison of collections", "#" * 40)
# Создаём 2 идентичных списка
languages_list_1 = ["Python", "C++", "C#", "Java"]
languages_list_2 = ["Python", "C++", "C#", "Java"]
# Проверяем их равенство
ic(languages_list_1 == languages_list_2)
# True

print("#" * 40)
# Создаём 2 идентичных словаря, различающихся порядком записи ключей
store_dict_1 = {"Яблоки": 158, "Мандарины": 178, "Хлеб": 56}
store_dict_2 = {"Хлеб": 56, "Яблоки": 158, "Мандарины": 178}
# Проверяем их равенство
ic(store_dict_1 == store_dict_2)
# True

print("#" * 100)
print("Logical operations")
print("#" * 100)

print("#" * 40, "Logical NOT", "#" * 40)
ic(not True)
# False
ic(not False)
# True
ic(not (5 == 10))
# True
ic(not ("abc" != "bca"))
# False

print("#" * 40, "Logical AND", "#" * 40)
a = 1
# Создаём первое условие
cond1 = 0 < a
# Создаём второе условие
cond2 = 4 > a
# Проверяем, будут ли выполняться два условия одновременно
ic(cond1 and cond2)
# True

print("#" * 40)
sym = "t"
# Проверяем, содержится ли символ в строке "python"
cond3 = sym in "python"
# Проверяем, содержится ли символ в строке "django"
cond4 = sym in "django"
# Проверяем, содержится ли символ в обеих строках
ic(cond3 and cond4)
# False

print("#" * 40, "Logical OR", "#" * 40)
word1 = "Institute"
word2 = "University"
target_string = "I graduated from the Moscow Aviation Institute in 2015, after which I got a job at…"
# Проверяем, содержится хотя бы одна из строк word1 или word2 в строке target_string
# Для проверки принадлежности используем оператор in
ic((word1 in target_string) or (word2 in target_string))
# True

print("#" * 40)
# Проверяем, что символ 't' есть хотя бы в одной из строк
ic(("t" in "python") or ("t" in "django"))
# True

print("#" * 40)
ic(not not not not True)
# True

print("#" * 40)
ic(not True or (True and not True))
# False


print("#" * 40)
ic(not False and True or False and not True)
# True

print("#" * 40, "Operator IS", "#" * 40)
a = "simple string"
b = a
# Смотрим на идентификаторы переменных a и b
ic(id(a), id(b))
# 140227942415216 140227942415216
# Проверяем равенство идентификаторов
ic(id(a) == id(b))
# True
# Проверяем эквивалентность двух объектов
ic(a is b)
# True

print("#" * 40)
c = 3
d = 9
# Смотрим на идентификатор переменной c
ic(id(c))
# 1889303357808
# Смотрим на идентификатор переменной d
ic(id(d))
# 1889303358000
# Проверяем эквивалентность двух объектов
ic(c is d)
# False

print("#" * 40)
e = 3
g = 3.0
f = "3"
ic(id(e))
ic(id(g))
ic(id(f))
ic(id(int(f)))
ic(e is int(f))
ic(e is g)

print("#" * 40)
x = 15.35
y = 15.35
# Смотрим на идентификатор переменной x
ic(id(x))
# 1887879819984
# Смотрим на идентификатор переменной y
ic(id(y))
# 1887879822608
# Проверяем равенство двух объектов
ic(x == y)
# True
# Проверяем эквивалентность двух объектов
ic(x is y)
# True

print("#" * 40)
x = 256
y = 256
# Проверяем равенство и эквивалентность двух объектов
ic(x == y, x is y)
# True True
w = 4589292
v = 4589292
# Проверяем равенство и эквивалентность двух объектов
ic(w == v, w is v)
# True True

print("#" * 100)
print("Entry of an element in a sequence")
print("#" * 100)

print("#" * 40)
orders = {
    "2022-10-10": ["F124", "D89D", "142L"],
    "2022-10-11": ["H241", "OR24", "BE14", "348F"],
    "2022-10-12": ["H429", "JAS2"],
}
target_order = "BE14"
# Проверяем вхождение строки target_order в список, хранящийся по ключу '2022-10-10'
ic(target_order in orders["2022-10-10"])
# False
# Проверяем вхождение строку target_order в список, хранящийся по ключу '2022-10-11'
ic(target_order in orders["2022-10-11"])
# True
# Проверяем вхождение строку target_order в список, хранящийся по ключу '2022-10-12'
ic(target_order in orders["2022-10-12"])
# False
# Объединяем условия для каждого заказа в одно
result = (
    (target_order in orders["2022-10-10"])
    or (target_order in orders["2022-10-11"])
    or (target_order in orders["2022-10-12"])
)
ic(result)
# True

print("#" * 40)
message = 14093530013530593
# print(5 not in message[:6])
# TypeError: 'int' object is not subscriptable
# print(5 not in str(message)[:6])
# TypeError: 'in <string>' requires string as left operand, not int
# Проверяем вхождение символа '5' в первые 6 символов строки message
message_is_useful = "5" not in str(message)[:6]
ic(message_is_useful)
# False

print("#" * 40, "Divisibility of numbers", "#" * 40)
available_packages = 105
total_count = 1677
# Проверяем, что все карандаши удастся распределить по упаковкам
ic(total_count % 13 == 0)
# True# Проверяем, достаточно ли у нас упаковок на складе
ic(total_count // 13 <= available_packages)
# False
# Создаём переменные под каждое условие
condition_1 = total_count % 13 == 0
condition_2 = total_count // 13 <= available_packages
# Проверяем, что условия выполняются одновременно
result = condition_1 and condition_2
ic(result)
# False

print("#" * 40, "Equality", "#" * 40)

name = ""
surname = ""
second_name = ""
# Incorrect
name = None
surname = None
second_name = None
ic(name)
ic(type(name))
# None
# <class 'NoneType'>
ic(id(name) == id(surname) and id(name) == id(second_name))
# True
# Плохо, так лучше не делать
ic(second_name == None)
# True
# Хорошо
ic(second_name is None)
# True

print("#" * 40)
lst = ["C++", "Python", "Java"]
append_result = lst.append("JavaScript")
ic(lst)
# ['C++', 'Python', 'Java', 'JavaScript']
ic(append_result)
# None

print("#" * 40)
product_dict = {"Сок яблочный": 15, "Сок тыквенный": 10, "Сок ананасовый": 5}
value = product_dict.get("Сок яблочный")
ic(value)
# 15
value = product_dict.get("Сок вишневый")
ic(value)
# None

print("#" * 100)
print("Condition operators")
print("#" * 100)

print("#" * 40, "Simple condition operator", "#" * 40)

print("#" * 40)
is_rainy = True  # дождь будет
# Реализуем условный оператор
# В блок if помещаем условие
if is_rainy:
    # брать зонт
    ic("Take an umbrella")
else:
    # не брать зонт
    ic("Don't take an umbrella")
# Брать зонт

print("#" * 40)
a = 2**10
b = 3**5
if a > b:
    # значение a > значения b
    ic("Value of variable a > value of variable b")
# Value of variable a > value of variable b

print("#" * 40)
a = 2**10
b = 3**5
# Реализуем условный оператор if-else
# В блок if помещаем условие
if a > b:
    # значение a > значения b
    ic("Value of variable a > value of variable b")
else:
    # значение a <= значения b
    ic("Value of variable a <= value of variable b")
# Value of variable a > value of variable b

print("#" * 40)
target_word = "and"
words = ["and", "or", "not"]
# Проверяем, что строка target_word есть в списке words
if target_word in words:
    # целевое слово есть в списке
    ic('String "{}" is in list'.format(target_word))
# String "and" is in list

print("#" * 40)
target_word = "on"
words = ["and", "or", "not"]
# Проверяем, что строка target_word есть в списке words
if target_word in words:
    # целевое слово есть в списке
    ic('String "{}" is in list'.format(target_word))
ic("{} — target_word".format(target_word))
ic("{} — list of words".format(words))

print("#" * 40)
a = 7
b = 9 + a
ic("a = F(", b, ")")

print("#" * 40)
s = 5
a = 10
if a > 0:
    s = s + a
else:
    s = s - a
ic(s)

print("#" * 40, "Nested condition operator", "#" * 40)

print("#" * 40)
is_rainy = True  # дождь будет
heavy_rain = False  # не сильный дождь

if is_rainy:
    # в данный блок дописали ещё один условный оператор
    if heavy_rain:
        # брать зонт
        ic("Take an umbrella")
    else:
        # надеть дождевик
        ic("Put on a raincoat")
else:
    # не брать зонт
    ic("Don't take an umbrella")
# Put on a raincoat

print("#" * 40)
credit_history = "good"  # кредитная история
deposit = True  # есть ли залог
guarantors = False  # есть ли поручители
credit = 500.0  # сумма долга
if credit_history == "bad":
    if deposit:
        if guarantors:
            ic("Issue a loan")
        else:
            ic("Not to issue a loan")
    else:
        ic("Not to issue a loan")
else:
    if credit < 1000:
        ic("Issue a loan")
    else:
        ic("Not to issue a loan")
# Issue a loan

print("#" * 40)
if (credit_history == "bad" and deposit and guarantors) or (
    credit_history == "good" and credit < 1000
):
    ic("Issue a loan")
else:
    ic("Not to issue a loan")

print("#" * 40, "Implicit cast to bool", "#" * 40)

print("#" * 40)
ic(bool(893), bool(-8), bool(0))
# True True False

print("#" * 40)
if 892:
    ic("Hello, world!")
else:
    ic("Goodbye, world!")
# Hello, world!

print("#" * 40)
if 0:
    ic("Hello, world!")
else:
    ic("Goodbye, world!")
# Goodbye, world!

print("#" * 40)
number = 3
if number != 0:
    ic(10 / number)
else:
    ic("You can't divide by zero")

print("#" * 40)
ic(bool("Hello, world"), bool(""))
# True False

print("#" * 40)
password = "e"
# Очень плохо
if len(password) == 0:
    ic("You forgot to enter your password")
else:
    ic("Password entered")
# Плохо
if password == "":
    ic("You forgot to enter your password")
else:
    ic("Password entered")
# Хорошо
if not password:
    ic("You forgot to enter your password")
else:
    ic("Password entered")

print("#" * 40)
ic(bool([1]), bool([]))
# True False

print("#" * 40)
orders_list = []
# Очень плохо
if len(orders_list) == 0:
    ic("You don't have any orders at the moment")
else:
    ic("You have current orders")
# Плохо
if orders_list == []:
    ic("You don't have any orders at the moment")
else:
    ic("You have current orders")
# Хорошо
if not orders_list:
    ic("You don't have any orders at the moment")
else:
    ic("You have current orders")

print("#" * 40, "Ternary operator", "#" * 40)
a = 42
b = 41

if a > b:
    result = a
else:
    result = b

ic(result)
# 42
result = a if a > b else b

ic(result)
# 42

print("#" * 40)
cust_age = 40
# Проверяем условие: возраст больше 60
if cust_age >= 60:
    # условие выполняется
    ic("Eligible for discount")
else:
    # условие не выполняется
    ic("Not eligible for discount")
# Not eligible for discount
cust_age = 40
# Реализуем тот же код через тернарный оператор
cust_discount = (
    "Eligible for discount" if cust_age >= 60 else "Not eligible for discount"
)
ic(cust_discount)
# Not eligible for discount

print("#" * 40)
answer_dict = {True: "Eligible for discount", False: "Not eligible for discount"}
cust_age = 40
ic(answer_dict[cust_age >= 60])
# Not eligible for discount

print("#" * 40)
lst = ["a", "b", "c"]
x = 5 if "f" in lst else None
ic(x)

print("#" * 100)
print("Practice")
print("#" * 100)

print(
    "#" * 40,
    "Using logical and comparison operators in a conditional statement",
    "#" * 40,
)
# не лучший способ
month = 1
if month == 3 or month == 4 or month == 5:
    ic("Spring")
# хорошо
if month in [3, 4, 5]:
    ic("Spring")

print("#" * 40)
if month in [3, 4, 5]:  # весна
    ic("Spring")
elif month in [6, 7, 8]:  # лето
    ic("Summer")
elif month in [9, 10, 11]:  # осень
    ic("Autumn")
elif month in [12, 1, 2]:  # зима
    ic("Winter")
else:  # некорректный номер месяца
    ic("Incorrect month number")

print("#" * 40, "Complex tasks", "#" * 40)

print("#" * 40)
dish_time_dict = {
    "Рамен с говядиной": 15,
    "Суши": 18,
    "Лагман с курицей": 20,
    "Лагман с говядиной": 24,
    "Плов с курицей": 28,
}
street_time_dict = {
    "Дзержинский": 39,
    "Солнечный": 40,
    "Заводской": 27,
    "Гагаринский": 43,
    "Кировский": 37,
    "Октябрьский": 34,
}
dish, street = "Рамен с говядиной", "Заводской"
street = "Заводской"
ic(street not in street_time_dict)
# True
if street not in street_time_dict:
    ic("Доставка в ваш район недоступна")
elif dish not in dish_time_dict:
    ic("Блюдо недоступно, закажите что-то другое")
else:
    # здесь будет дальнейший код
    print()

dish_time = dish_time_dict[dish]  # время приготовления блюда
street_time = street_time_dict[street]  # время доставки
full_time = dish_time + street_time  # общее время доставки
delay = full_time - 60  # задержка
if delay <= 0:
    # задержка не положительна
    ic("Заказ будет доставлен вовремя")
else:
    # задержка положительная
    ic("Курьер задержится на {} минут".format(delay))

if street not in street_time_dict:
    # неизвестный район
    ic("Доставка в ваш район недоступна")
elif dish not in dish_time_dict:
    # неизвестное блюдо
    ic("Блюдо недоступно, закажите что-то другое")
else:
    # район доступен для доставки и блюдо известно
    dish_time = dish_time_dict[dish]  # время приготовления блюда
    street_time = street_time_dict[street]  # время доставки
    full_time = dish_time + street_time  # общее время доставки
    delay = full_time - 60  # задержка
    if delay <= 0:
        # задержка не положительна
        ic("Заказ будет доставлен вовремя")
    else:
        # задержка положительная
        ic("Курьер задержится на {} минут".format(delay))

dish, street = "Рамен с говядиной", "Заводской"
# Заказ будет доставлен вовремя

dish, street = "Плов с курицей", "Солнечный"
# "Курьер задержится на 8 минут"

dish, street = "Бургер с говядиной", "Солнечный"
# "Блюдо недоступно, закажите что-то другое"

print("#" * 40)
purchases = ["Adidas", "Nike"]
prices = {"Adidas": 4298, "Nike": 6550, "Puma": 4490, "Asics": 3879}
sale = 5
result_str = "Стоимость заказа составила: {}"
price = None
total = None

if not purchases:
    ic("Ваша корзина пуста")
elif len(purchases) == 1:
    price = prices[purchases[0]]
    ic(result_str.format(price))
else:
    result_str = "Стоимость заказа составила: {}. С учетом скидки в {}% — {}"
    if purchases[0] == purchases[1]:
        sale = 10
    price = prices[purchases[0]] + prices[purchases[1]]
    total = (100 - sale) / 100 * price
    ic(result_str.format(price, sale, total))

print("#" * 100)
print("Exceptions")
print("#" * 100)

print("#" * 40, "Exception handling", "#" * 40)
# print("#" * 40)
# ic("Before exception")
# # Теперь пользователь сам вводит числа для деления
# a = int(input("a: "))
# b = int(input("b: "))
# # Здесь может возникнуть исключение деления на ноль
# c = a / b
# # Печатаем c = a / b если всё хорошо
# ic(c)
# ic("After exception")

# print("#" * 40)
# # Добавляем конструкцию try-except для отлова нашей ошибки
# try:
#     ic("Before exception")
#     # Теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     # Здесь может возникнуть исключение деления на ноль
#     c = a / b
#     # Печатаем c = a / b если всё хорошо
#     ic(c)
# # Добавляем тип именно той ошибки которую хотим отловить.
# except ZeroDivisionError as e:
#     # Выводим информацию об ошибке
#     ic(e)
#     ic("After exception")
# ic("After after exception")

print("#" * 40)
# Добавляем конструкцию try-except для отлова нашей ошибки
try:
    ic("Before exception")  # Перед исключением
    # Теперь пользователь сам вводит числа для деления
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    # Печатаем c = a / b, если всё хорошо
    ic(c)
# Добавляем тип именно той ошибки которую хотим отловить.
except ZeroDivisionError as e:
    ic("After exception")  # После исключения
# код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т. е. не произошло никакого исключения)
else:
    ic("Everything's fine!")  # Всё отлично!
# код в блоке finally выполнится в любом случае при выходе из try-except
finally:
    ic("Finally finished!")  # Наконец-то завершено!

ic("After After exception")  # После после исключения

print("#" * 40, "Exception Generation", "#" * 40)

age = int(input("How old are you?"))
# Проверяем, что возраст пользователя корректный
if 0 <= age > 100:
    # Намеренно вызываем ошибку, в скобках указываем текст ошибки
    raise ValueError("You are too old or don't exist")
# Возраст выводится только в том случае, если пользователь ввёл правильный возраст.
ic("You are {} years old!".format(age))

print("#" * 40)
# Добавляем конструкцию try-except для отлова нашей ошибки
try:
    age = int(input("How old are you?"))
    # Проверяем, что возраст пользователя корректный
    if age > 100 or age <= 0:
        # Намеренно вызываем ошибку, в скобках указываем текст ошибки
        raise ValueError("You are too old or don't exist")
# Ловим исключение ValueError
except ValueError:
    # В случае возникновения исключения выводим сообщение
    ic("Wrong age")
# В блоке else прописываем часть, которая выполняется, если блок try отработал без ошибок
else:
    # Возраст выводится только в том случае, если пользователь ввёл правильный возраст.
    ic("You are {} years old!".format(age))
