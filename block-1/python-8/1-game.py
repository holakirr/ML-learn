"""Игра угадай число"""

import numpy as np
from icecream import ic

number = np.random.randint(1, 101)  # загадали число

# количество попыток
tries = 0

while True:
    tries += 1
    predict = int(input("Угадай число от 1 до 100: "))
    if number == predict:
        ic(f"Вы угадали, поздравляем! Это число {number}. Количество попыток: {tries}")
        break
    elif number > predict:
        ic("Ваше число меньше загаданного")
    else:
        ic("Ваше число больше загаданного")
