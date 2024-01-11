from icecream import ic

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
