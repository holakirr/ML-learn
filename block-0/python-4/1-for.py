from icecream import ic

users = ["John", "Artur", "Kate"]


def send_message(user):
    ic(f"Hello, {user}!")


print("#" * 100)
print("For")
print("#" * 100)

send_message(users[0])  # отправка 1-му пользователю
send_message(users[1])  # отправка 2-му пользователю
send_message(users[2])  # отправка 3-му пользователю
# и так ещё много-много раз

print("#" * 40)
for user_id in users:  # для каждого из пользователей
    send_message(user_id)  # отправить уведомление

print("#" * 40)
# Создаём цикл по всем пользователям из списка users
for user_id in users:
    # Начало блока кода с телом цикла
    send_message(user_id)  # Отправляем уведомление о скидках
    # Конец блока кода с телом цикла
# Код, который будет выполняться после цикла
# Выводим на экран сообщение об успешной отправке
ic("All messages have been sent")

print("#" * 40)
# Определяем итерируемый объект
my_list = [5, 9, 19]
# Подставляем его в шаблон для цикла и записываем имя переменной цикла
for element in my_list:
    # Указываем необходимые действия в тело цикла
    ic("Element", element)
# Будет выведено:
# Element 5
# Element 9
# Element 19

print("#" * 40)
# Задаём список доходов семьи Быковых
incomes = [120, 38.5, 40.5, 80]


# Задаём начальное значение суммы доходов
S = 0
# Создаём цикл for, в котором будем проходиться по элементам списка incomes.
# income — текущее значение элемента списка
for income in incomes:
    # Выводим текущее значение переменной income
    ic("Current income", income)
    # Выводим текущее значение переменной S
    ic("Current S", S)
    # Увеличиваем сумму доходов на значение income
    # Равносильно S = S + income
    S += income
    # Выводим обновлённое значение переменной S
    ic("New S", S)
    # Выводим пустую строку для красивого отображения
    print()
# Выводим результат
ic("Answer: s=", S)

print("#" * 40)
# Создаём накопительную переменную, в которой будем считать сумму.
S = 0
# Задаём N — последний элемент последовательности
N = 5
# Создаём цикл for, которым будем проходить по всем числам от 1 до N (включительно).
# Равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
for i in range(1, N + 1):
    # Выводим значение суммы на текущем шаге
    ic("Current S: ", S)
    # Выводим текущее число
    ic("Current number: ", i)
    # Суммируем текущее число i и перезаписываем значение суммы
    # Равносильно S = S + i
    S += i
    # Выводим значение суммы после сложения
    ic("Sum after addition: ", S)
    # Выводим строчку для визуального разделения результатов
    ic("---")
# Выводим ответ в формате “ответ: сумма равна =”
ic("Answer: sum = ", S)

print("#" * 40)
# Задаём список значений массы товаров
weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]
# Задаём максимальное значение веса груза
max_weight = 100
# Задаём начальный номер груза
num = 1
# Создаём цикл по элементам списка со значениями массы товаров
# weight — текущее значение веса
for weight in weight_of_products:
    # Если текущий вес меньше максимального,
    if weight < max_weight:
        # выводим номер груза, его вес и отправляем его в легковую машину.
        ic("Product {}, weight: {} -passenger car".format(num, weight))
    else:
        # В противном случае
        # выводим номер груза, его вес и отправляем его в грузовую машину.
        ic("Product {}, weight: {} -truck".format(num, weight))
    # Увеличиваем значение номера груза на 1
    num += 1

print("#" * 40)
# Задаём список значений массы товаров
weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]
# Задаём максимальное значение веса груза
max_weight = 100
# Вычисляем длину списка
N = len(weight_of_products)
# Создаём цикл по последовательности чисел от 0 до N (не включая N)
# i — текущее значение последовательности
for i in range(N):
    # Обращаемся к элементу по индексу и сравниваем его с максимумом
    if weight_of_products[i] < max_weight:
        # Если текущий вес меньше максимального,
        # выводим номер груза, его массу и отправляем его в легковую машину.
        ic("Product {}, weight: {} -passenger car".format(i + 1, weight_of_products[i]))
    else:
        # В противном случае
        # выводим номер груза, его массу и отправляем его в грузовую машину
        ic("Product {}, weight: {} -truck".format(i + 1, weight_of_products[i]))
