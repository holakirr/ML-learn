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
print(res_string.format(*find_min_max(format_input_string(input_string))))
