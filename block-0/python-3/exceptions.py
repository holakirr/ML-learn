from icecream import ic

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
