from icecream import ic

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
