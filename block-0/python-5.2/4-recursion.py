from icecream import ic

print("#" * 100)
print("Recursion")
print("#" * 100)


def sum_lst(lst):
    # Выводим текущее значение lst
    ic(lst)
    # Задаём условие выхода из рекурсии
    if len(lst) == 0:
        return 0
    # Во всех других случаях возвращаем
    # сумму первого элемента списка
    # и результат суммирования оставшихся
    return lst[0] + sum_lst(lst[1:])


my_lst = [10, 21, 24, 12]
ic(sum_lst(my_lst))
## Будет выведено:
## [10, 21, 24, 12]
## [21, 24, 12]
## [24, 12]
## [12]
## []
## 67

print("#" * 100)
print("Call stack")
print("#" * 100)

# Введите свое решение ниже
multiply_lst = lambda lst: 1 if not lst else lst[0] * multiply_lst(lst[1:])

ic(multiply_lst([1, 5, 2, 1.5]))
## 15
ic(multiply_lst([]))
## 1
ic(multiply_lst([10, 21, 24, 12]))
## 60480

print("#" * 40)
inv_sum_list = lambda lst: 0 if not lst else 1 / lst[0] + inv_sum_list(lst[1:])
ic(inv_sum_list([10, 4, 8]))
## 0.475

ic(inv_sum_list([10, 1, 2, 4, 8]))
## 1.975

ic(inv_sum_list([]))
## 0

print("#" * 40)


def factorial(n):
    # Задаём условия выхода из рекурсии:
    if n == 0:
        return 1
    if n == 1:
        return 1
    # Во всех других случаях возвращаем
    # произведение текущего числа n и функции от n-1
    return factorial(n - 1) * n


ic(factorial(0))
ic(factorial(3))
ic(factorial(5))
## Будет напечатано:
## 1
## 6
## 120

# Let's make it lambda
factorial = lambda n: 1 if n == 0 else factorial(n - 1) * n

print("#" * 40)


def combination(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


ic(combination(n=10, k=5))
## 252.0
ic(combination(n=12, k=3))
## 220.0
ic(combination(n=1, k=1))
## 1.0
ic(combination(n=0, k=0))
## 1.0

# Let's make it lambda
combination = lambda n, k: factorial(n) / (factorial(n - k) * factorial(k))

print("#" * 40)


# Fibonacci function


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


ic(fib(1))
# 1
ic(fib(2))
# 1
ic(fib(6))
# 8

# Let's make it lambda
fib = lambda n: 1 if n == 1 or n == 2 else fib(n - 1) + fib(n - 2)
