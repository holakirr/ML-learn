from typing import Dict

from icecream import ic

print("#" * 100)
print("Type Conversion")
print("#" * 100)

print("#" * 40, "Int and FLoat", "#" * 40)
int_var = 10
# присвоим переменной int_var целое число — 10.
float_var = float(10)
# запишем в переменную float_var преобразованное в вещественное целое число 10.
ic(int_var)
# 10
ic(float_var)
# 10.0

print("#" * 40)
float_var1 = 10.2
# запишем в переменную float_var1 вещественное число
float_var2 = float(5)
# запишем в переменную float_var2 преобразованное в вещественное число 5
ic(float_var1 + float_var2)
# 15.2

print("#" * 40)
float_var1 = 10.2
# запишем в переменную float_var1 вещественное число
int_var2 = 5
# присвоим переменной int_var2 целое число — 5.
ic(float_var1 + int_var2)
# 15.2

print("#" * 40)
float_var = 7.5
# запишем в переменную float_var вещественное число
int_var = int(7.5)
# запишем в переменную int_var преобразованное в целое число число 7.5
ic(int_var)
# 7

print("#" * 40)
a = 3
b = float(a)
ic(b)
# 3.0

print("#" * 40)
num1 = 3
num2 = 3.5
sum1 = num1 + num2
sum2 = float(num1) + num2
ic(sum1)
# 6.5
ic(sum2)
# 6.5

print("#" * 40, "Int to String", "#" * 40)
int_var = 5
str_var = str(int_var)
ic(str_var)
# '5'

print("#" * 40)
str_var1 = "I am"
int_var = 10
str_var2 = "years old"
# ic(str_var1 + int_var + str_var2)
# TypeError: can only concatenate str (not "int") to str

ic(str_var1 + str(int_var) + str_var2)
# 'I am10years old'

print("#" * 40)
int_one = 1
str_one = str(int_one)
print(str_one)
# 1

print("#" * 40)
str_age_begin = "my age is "
int_age = 18
result_string = str_age_begin + str(int_age)
print(result_string)
# my age is 18

print("#" * 40)
str_brothers_begin = "I have "
count = 5
str_brothers_end = " brothers"
result_sentence = str_brothers_begin + str(count) + str_brothers_end
print(result_sentence)
# I have 5 brothers

print("#" * 40, "String to Int", "#" * 40)
my_date = "1990"
mom_date = "1957"
# mom_date - my_date
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
my_date = "1990.0"
int_mom_date = int(mom_date)
float_my_date = float(my_date)
ic(float_my_date - int_mom_date)
# 33.0

print("#" * 40)
my_date = "1990.0"
# int_my_date = int(my_date)
# ValueError: invalid literal for int() with base 10: '1990.0'

print("#" * 40)
s = "hello world"
# int(s)
# ValueError: invalid literal for int() with base 10: 'hello world'

print("#" * 40)
s = "10"
ic(int(s))

print("#" * 40)
s = "11"
ic(float(s))

print("#" * 40)
s = "50.4"
# ic(int(s))
# ValueError: invalid literal for int() with base 10: '50.4'

print("#" * 40, "Tuples and Lists", "#" * 40)
dictionary = {"Anne": 15, "Sam": 30, "Marie": 22}
only_keys = dictionary.keys()
ic(only_keys)
# dict_keys(["Anne", "Sam", "Marie"])

# only_keys = only_keys + ["Tom", "Curt"]
# TypeError: unsupported operand type(s) for +: 'dict_keys' and 'list'
only_keys = list(only_keys)
only_keys = only_keys + ["Tom", "Curt"]
ic(only_keys)
# ["Anne", "Sam", "Marie", "Tom", "Curt"]

print("#" * 40)
d: Dict[tuple, str] = {("Amanda", 22, "NY"): "3rd place"}
input_list = ["Collin", 23, "LA"]
# создаём новый ключ для словаря. Но пока этот ключ в виде списка.
input_place = "2nd place"
# также определяем значение для нового ключа.

# d[input_list] = input_place
# TypeError: unhashable type: 'list'
input_list_as_tuple = tuple(input_list)
# преобразуем список в кортеж через конструктор типов tuple()

d[input_list_as_tuple] = input_place
# добавляем новый ключ и значение в словарь и выводим результат
ic(d)
# {("Amanda", 22, "NY"): "3rd place", ("Collin", 23, "LA"): "2nd place"}

print("#" * 40)
list1 = list(range(1, 6))
tpl1 = tuple(list1)
ic(tpl1)

print("#" * 40)
tpl1 = ("a", "b", "c", "d", "e")
list2 = list(tpl1)
ic(list2)
