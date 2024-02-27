from icecream import ic

print("#" * 100)
print("Practice")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)
input_string1 = input("Введите 1-ую последовательность идентификаторов: ")
input_string2 = input("Введите 2-ую последовательность идентификаторов: ")
# ваш код здесь


# Preparing data for the function find_intersection (Creating list of integers from the string and then making a set of unique integers from the list)
def prepare_input_string(input_string) -> set[int]:
    return set(map(int, input_string.split(", ")))


# Resulting function
def find_intersection(input_string1, input_string2):
    try:
        set1 = prepare_input_string(input_string1)
        set2 = prepare_input_string(input_string2)
        ic(list(set1.intersection(set2)))
    except ValueError:
        ic("Некорректный ввод")


find_intersection(input_string1, input_string2)

print("#" * 40, "Task 2", "#" * 40)
input_string = input("Введите последовательность чисел: ")


# Replacing "," with "." for correct number spelling and splitting the string by " " and then converting the list of strings to the list of floats
def format_input_string(input_string: str) -> list[int]:
    res = []
    for num in list(input_string.replace(",", ".").split(" ")):
        try:
            res.append(float(num))
        except:
            continue
    return res


# Finding min and max values in the list of numbers
def find_min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


res_string = "Minimum: {}\nMaximum: {}"
ic(res_string.format(*find_min_max(format_input_string(input_string))))


print("#" * 40, "Task 3", "#" * 40)
input_string = input("Введите последовательность чисел: ")
# ваш код здесь


def find_median(input_string: str) -> None:
    try:
        # Preparing data for the future calculations
        nums = list(map(int, input_string.split(", ")))
        nums.sort()
        res: float
        # Finding median
        length = len(nums)
        if length % 2 == 0:
            res = (nums[length // 2 - 1] + nums[length // 2]) / 2
        else:
            res = nums[length // 2]
        ic("Median: {}".format(float(res)))
    except ValueError:
        ic("Некорректный ввод")
        return


find_median(input_string)

print("#" * 40, "Task 4", "#" * 40)
input_string: str = input("Введите число словами: ")
# ваш код здесь
number_word_dict = {
    "ты": 1000,
    "м": 1000000,
    "сто": 100,
    "двес": 200,
    "трис": 300,
    "четырес": 400,
    "пятьс": 500,
    "шестьс": 600,
    "семьс": 700,
    "восемьс": 800,
    "девятьс": 900,
    "одинн": 11,
    "двен": 12,
    "трин": 13,
    "четырн": 14,
    "пятн": 15,
    "шестн": 16,
    "семн": 17,
    "восемн": 18,
    "девятн": 19,
    "двад": 20,
    "трид": 30,
    "сор": 40,
    "пятьд": 50,
    "шестьд": 60,
    "семьд": 70,
    "восемьд": 80,
    "девяно": 90,
    "дес": 10,
    "н": 0,
    "о": 1,
    "дв": 2,
    "т": 3,
    "ч": 4,
    "п": 5,
    "ш": 6,
    "с": 7,
    "в": 8,
    "д": 9,
}


def transform_string_to_integer(input_string: str) -> int:
    units = 0
    thousands = 0
    millions = 0

    # Iterating through the list of words
    for word in input_string.split(" "):
        # Iterating through the dictionary of words and their numbers
        for key in number_word_dict:
            if word.startswith(key):
                # Separately calculating millions, thousands and units
                if key == "м":
                    millions = units * number_word_dict[key]
                    units = 0
                elif key == "ты":
                    thousands = units * number_word_dict[key]
                    units = 0
                else:
                    units += number_word_dict[key]
                break
    # Returning the sum of millions, thousands and units
    return units + thousands + millions


ic(transform_string_to_integer(input_string))
