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
