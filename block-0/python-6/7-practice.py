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
