from icecream import ic

print("#" * 100)
print("Advanced arguments passing")
print("#" * 100)


def root(value, n=2, verbose=False):
    result = value ** (1 / n)
    if verbose:
        # Аргументы в функции print,
        # перечисленные через запятую,
        # печатаются через пробел
        ic("Root of power", n, "from", value, "equals", result)
    return result


# Посчитаем корень из 25 с аргументами по умолчанию
ic(root(25))
# Будет напечатано:
# 5.0

# Посчитаем кубический корень из 27 с verbose по умолчанию
ic(root(27, 3))
# Будет напечатано:
# 3.0

# Посчитаем кубический корень из 27 с verbose=True
ic(root(27, 3, True))
# Будет напечатано:
# Root of power 3 from 27 equals 3.0
# 3.0

ic(root(25, verbose=True))
# Будет напечатано:
# Root of power 2 from 25 equals 5.0
# 5.0

# ic(root(verbose=True, 25))
# Будет напечатано:
# SyntaxError: positional argument follows keyword argument

# Подробно считаем корень степени 4 из 81
ic(root(81, verbose=True, n=4))
# Будет напечатано:
# Root of power 4 from 81 equals 3.0
# 3.0

# Написали value=81 после именованных:
ic(root(verbose=True, n=4, value=81))
# Будет напечатано:
# Root of power 4 from 81 equals 3.0
# 3.0

print("#" * 40)

print("Shopping list:", end=" ")
print("bread", "butter", "eggs", sep=", ")
# Будет напечатано:
# Shopping list: bread butter eggs
