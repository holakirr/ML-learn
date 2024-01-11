from icecream import ic

print("#" * 100)
print("Scope")
print("#" * 100)

print("#" * 40, "Scope of function", "#" * 40)


# Объявляем внешнюю функцию outer()
def outer():
    # Печатаем информацию о вызове внешней функции
    ic("Called outer function")

    # Объявляем внутреннюю функцию inner()
    def inner():
        # Печатаем информацию о вызове внутренней функции
        ic("Called inner function")

    # Вызываем внутреннюю функцию inner()
    inner()


outer()

print("#" * 40)


# Задаём внешнюю функцию
def print_root(value, n=2):
    # Задаём внутреннюю функцию
    # Она будет являться вспомогательной
    def root(value, n=2):
        result = value ** (1 / n)
        return result

    # Получаем результат из внутренней функции
    res = root(value, n)
    # Печатаем результат и не возвращаем его
    ic(f"Root of power {n} from {value} equals {res}")


print_root(9, 2)
print_root(27, 3)
# print(root(81, 4))
# Возникнет ошибка:
# NameError: name 'root' is not defined

print("#" * 40)


def get_count_unique_symbols(s):
    return len(set([*s.lower().replace(" ", "")]))


ic(get_count_unique_symbols("Это простая строка"))
## 9
ic(get_count_unique_symbols("This is a simple string"))
## 12

print("#" * 40)


def get_min_string(s1, s2):
    get_count_unique_symbols = lambda s: len(set([*s.lower().replace(" ", "")]))
    if get_count_unique_symbols(s1) == get_count_unique_symbols(s2):
        return (s1, s2)
    return s2 if get_count_unique_symbols(s1) > get_count_unique_symbols(s2) else s1


ic(get_min_string("Это простая строка", "This is a simple string"))

print("#" * 40, "Scope of variable", "#" * 40)
ic("Built-in <- Global <- Enclosed <- Local")


# Объявляем внешнюю функцию для регистрации сотрудников
def register_employee(name, surname):
    # Объявляем функцию для промежуточных вычислений
    def create_full_name():
        # Функция использует внешние переменные name и surname
        sep = " "  # Разделитель между именем и фамилией
        result = name + sep + surname  # Вычисляем полное имя
        return result

    # Вызываем внутреннюю функцию
    full_name = create_full_name()
    # print(result)
    ## Возникнет ошибка:
    ## NameError: name 'result' is not defined
    # Выводим результат на экран, используя внешнюю переменную company_name
    ic("Employee {} is registered with the company {}".format(full_name, company_name))


company_name = "TheBlindMice"  # Название компании
register_employee("John", "Doe")  # Вызов функции

## Будет выведено
## Employee John Doe is registered with the company TheBlindMice

# print(full_name)
## Возникнет ошибка:
## NameError: name 'full_name' is not defined
