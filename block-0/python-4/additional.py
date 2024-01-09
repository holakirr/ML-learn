from icecream import ic

print("#" * 100)
print("Additional possibilities")
print("#" * 100)

# Условие задачи. У нас есть список ежедневной динамики числа пользователей приложения.
# Если элемент списка положительный, то число новых пользователей больше числа ушедших пользователей (прирост).
# Если элемент списка отрицательный, то число ушедших пользователей больше числа новых (отток).
print("#" * 40, "Enumerate", "#" * 40)

# First solution
# Заданный список динамики числа пользователей
user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# Задаём номер дня
number = 1
# Создаём цикл по элементам списка user_dynamics
for dynamic in user_dynamics:  # dynamic — текущее значение из списка
    # Выводим номер дня и динамику на этот день
    ic("Day {} : {}".format(number, dynamic))
    # Увеличиваем номер дня
    number += 1
# Будет выведено:
# Day 1 : -5
# Day 2 : 2
# Day 3 : 4
# Day 4 : 8
# Day 5 : 12
# Day 6 : -7
# Day 7 : 5

print("#" * 40)
# Second solution
# Заданный список динамики числа пользователей
user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# Вычисляем длину списка
N = len(user_dynamics)
# Создаём цикл по элементам последовательности от 0 до N (не включая N)
for i in range(N):  # i — текущий индекс
    # Выводим номер дня и динамику на этот день
    ic("Day {} : {}".format(i + 1, user_dynamics[i]))
# Будет выведено:
# Day 1 : -5
# Day 2 : 2
# Day 3 : 4
# Day 4 : 8
# Day 5 : 12
# Day 6 : -7
# Day 7 : 5

print("#" * 40)
# Third solution - Enumerate
# Заданный список динамики числа пользователей
user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# Создаём цикл по индексам и элементам списка
# i — индекс текущего элемента, dynamic — текущее значение из списка
for i, dynamic in enumerate(user_dynamics):
    # Выводим номер дня и динамику на этот день
    ic("Day {} : {}".format(i + 1, dynamic))
# Будет выведено:
# Day 1 : -5
# Day 2 : 2
# Day 3 : 4
# Day 4 : 8
# Day 5 : 12
# Day 6 : -7
# Day 7 : 5

print("#" * 40, "Break", "#" * 40)
# Условие задачи. Мы разрабатываем игру, и в ней предусмотрен инвентарь с ограниченным числом ячеек. Переменная inventory описывает список вещей, которые хранятся у игрока в инвентаре. Пусть изначально инвентарь пуст. У игрока есть только три свободные ячейки инвентаря.

# Список вещей, которые он хочет положить, хранится в переменной to_inventory
to_inventory = [
    "Blood Moon Sword",
    "Sunset-colored sword",
    "Bow of Stars",
    "Gain Stone",
]
# Необходимо написать программу, которая переносит вещи из списка to_inventory в список inventory, но если количество этих вещей превысит 3, то выводится предупреждение и перенос вещей заканчивается
# Список вещей, которые нужно положить в инвентарь.
to_inventory = [
    "Blood Moon Sword",
    "Sunset-colored sword",
    "Bow of Stars",
    "Gain Stone",
]
# Задаём пустой инвентарь
inventory = []
# Создаём цикл по элементам списка to_inventory
# item — текущий элемент списка
for item in to_inventory:
    # Проверяем условие, что инвентарь уже заполнен.
    if len(inventory) == 3:
        # Если условие выполняется,выводим предупреждение об ошибке.
        ic("Inventory is full!")
        # Завершаем работу цикла
        break
    # Если цикл не завершился добавляем предмет в инвентарь
    inventory.append(item)
# Выводим результирующий инвентарь
ic(inventory)
# Будет выведено:
# Inventory is full!
# ['Blood Moon Sword', 'Sunset-colored sword', 'Bow of Stars']

print("#" * 40)

# Условие задачи. В теории шифрования очень активно используются степени числа. Берётся число и несколько раз возводится в некоторую степень. Для дешифрации нужно определить, какое число было задано изначально.
# Например, изначально задано простое число 3, его возвели в степень 4 и получили число 81.
# Необходимо написать программу, которая проверяет, что число n является степенью числа 3.
# Задаём число
n = 27
# Создаём бесконечный цикл
while True:
    # Проверяем условие, что остаток от деления на 3 равен 0.
    if n % 3 == 0:
        # Если условие выполняется, новое число — результат целочисленного деления на 3.
        n = n // 3
        # Проверяем условие, что в результате деления получили 1.
        if n == 1:
            # Выводим утвердительное сообщение
            ic("n - is the power of the number 3!")
            # Выходим из цикла
            break
    else:
        # В противном случае выводим сообщение-опровержение
        ic("n - is not the power of the number 3!")
        # Выходим из цикла
        break
# Будет выведено:
# n - is the power of the number 3!

print("#" * 40, "Continue", "#" * 40)
# Условие задачи. Дан словарь клиентов и статус их программы скидок. Ключами словаря являются идентификаторы клиентов, а значениями — статусы программы скидок ('yes' — активен, 'no' — неактивен).
client_status = {103303: "yes", 103044: "no", 100423: "yes", 103032: "no", 103902: "no"}
# В честь Нового года магазин хочет отправить подарочные сертификаты всем, у кого активен статус программы скидок.
# Необходимо написать программу, которая выводит идентификаторы клиентов, которым полагается подарочный сертификат.
# Заданный словарь
client_status = {103303: "yes", 103044: "no", 100423: "yes", 103032: "no", 103902: "no"}
# Создаём цикл по ключам словаря client_status
for user_id in client_status:  # user_id — текущий ключ словаря
    if client_status[user_id] == "no":
        # Если текущий статус == 'no', переходим на следующую итерацию
        continue
    else:
        # В противном случае выводим сообщение об отправке сертификата
        ic("Send present user", user_id)
# Будет выведено:
# Send present user 103303
# Send present user 100423

print("#" * 40, "Pass", "#" * 40)
# Задан список
lst = [1, 2, 3, 4, 5]
# Создаём цикл по элементам списка
for i in lst:
    if i > 3:
        # Если i больше 3, ничего не делаем
        pass
    else:
        # В противном случае выводим элемент
        ic(i)

print("#" * 100)
print("Practical use")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)
# Условие задачи. Подсчитать количество вхождений каждого символа в заданном тексте. В результате работы программы должен быть сформирован словарь, ключи которого — символы текста, а значения — количество вхождений символа в тексте.
text = """
The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well.

Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled `ORANGE MARMALADE', but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as she fell past it.

`Well!' thought Alice to herself, `after such a fall as this, I shall think nothing of tumbling down stairs! How brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the house!' (Which was very likely true.)
"""
# Приводим текст к нижнему регистру
text = text.lower()
# Заменяем пробелы на пустые строки
text = text.replace(" ", "")
# Заменяем символы переноса строки на пустые строки
text = text.replace("\n", "")
# Выводим результирующий текст
ic(text)
count_dict = {}
for symbol in text:
    if symbol in count_dict:
        count_dict[symbol] += 1
    else:
        count_dict[symbol] = 1
ic(count_dict)

print("#" * 40, "Task 2", "#" * 40)
# Условие задачи. Подсчитать количество вхождений каждого слова в заданном тексте. В результате работы программы должен быть сформирован словарь, ключи которого — слова текста, а значения — количество вхождений слов в тексте.
text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""
# Приводим текст к нижнему регистру и удаляем знаки препинания
text = (
    text.lower()
    .replace("\n", " ")
    .replace(";", "")
    .replace(".", "")
    .replace(",", "")
    .replace("'", "")
)
# Выводим результат
ic(text)
word_list = text.split()
count_dict = {}
for word in word_list:
    if len(word) < 1:
        continue
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1
ic(count_dict)
