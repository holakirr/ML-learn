from icecream import ic

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
