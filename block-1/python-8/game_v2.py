"""
Игра угадай число
Пользователь загадывает число от 1 до 100, а затем компьютер угадывает его.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """
    Generates random numbers until the specified number is guessed.

    Parameters:
        number (int): The number to be guessed.

    Returns:
        int: The number of attempts it took to guess the specified number.
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count


def score_game(random_predict) -> None:
    """Function to calculate the average number of 1000 attempts to guess the number.

    Args:
        random_predict (_type_): predict function

    Returns:
        int: average number of attempts
    """
    tries_lst = []
    np.random.seed(1)  # making the experiment reproducible
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        tries_lst.append(random_predict(number))

    score = int(np.mean(tries_lst))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")


if __name__ == "__main__":
    # print(f"Количество попыток: {random_predict(np.random.randint(1, 101))}")
    score_game(random_predict)
