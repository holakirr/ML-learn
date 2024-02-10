from icecream import ic

print("#" * 100)
print("Operands")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)


def check_number_sign(number):
    return 1 if number > 0 else -1 if number < 0 else 0


ic(check_number_sign(5290))
# 1
ic(check_number_sign(-983))
# - 1
ic(check_number_sign(0))
# 0

print("#" * 40, "Task 2", "#" * 40)


def find_min_number(a, b, c):
    if a < b and a < c:
        return a
    else:
        if b < c:
            return b
        else:
            return c


ic(find_min_number(130, 122, 19))
# 19
ic(find_min_number(10.9, 12.2, 18.4))
# 10.9

print("#" * 40, "Task 3", "#" * 40)


def find_max_number(a, b, c):
    if a > b and a > c:
        return a
    else:
        if b > c:
            return b
        else:
            return c


def sum_min_numbers(a, b, c):
    return a + b + c - find_max_number(a, b, c)


ic(sum_min_numbers(1, 2, 3))
# 3
ic(sum_min_numbers(1, 2, -10))
# -9

print("#" * 40, "Task 4", "#" * 40)


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Zero division error!")


ic(division(189, 36))
# 5.25
ic(division(1, 0))
# Zero division error!
# None

print("#" * 40, "Task 5", "#" * 40)


def get_prediction(x1, x2):
    if x1 < 20:
        if x2 < 200:
            return 300.5
        else:
            return 65.7
    else:
        if x2 < 170:
            if x1 < 40:
                return -64.1
            else:
                return 0.7
        else:
            return 1023


ic(get_prediction(x1=15, x2=150))
# 300.5
ic(get_prediction(x1=15, x2=350))
# 65.7
ic(get_prediction(x1=35, x2=100))
# -64.1
ic(get_prediction(x1=175, x2=100))
# 0.7
ic(get_prediction(x1=175, x2=200))
# 1023
