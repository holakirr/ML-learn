from icecream import ic

print("#" * 100)
print("Practice")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)
car_dict = {
    "car_ID": [123, 117, 111, 82, 101, 96, 156, 2, 58, 49],
    "fueltype": [
        "gas",
        "diesel",
        "diesel",
        "gas",
        "gas",
        "gas",
        "gas",
        "gas",
        "gas",
        "gas",
    ],
    "horsepower": [68, 95, 95, 88, 97, 69, 62, 111, 101, 176],
    "price": [
        7609.0,
        17950.0,
        13860.0,
        8499.0,
        9549.0,
        7799.0,
        8778.0,
        16500.0,
        13645.0,
        35550.0,
    ],
}

# mean_price = 13973.9
# count_diesel = 2
# min_horsepower = 62

mean_price = sum(car_dict["price"]) / len(car_dict["price"])
count_diesel = car_dict["fueltype"].count("diesel")
min_horsepower = min(car_dict["horsepower"])
ic(mean_price, count_diesel, min_horsepower)

print("#" * 40, "Task 2", "#" * 40)


def check_duplicates(lst):
    return len(lst) != len(set(lst))


lst = [0, 0, 1, 2, 3, 4, 5, 5, 6, 7]
ic(check_duplicates(lst))
# True

lst = list(range(0, 15))
ic(check_duplicates(lst))
# False

print("#" * 40, "Task 3", "#" * 40)


def swap_places(lst):
    return [lst[-1]] + lst[1:-1] + [lst[0]]


ic(swap_places([1, 2, 3]))
## [3, 2, 1]
ic(swap_places([1, 2, 3, 4, 5]))
## [5, 2, 3, 4, 1]
ic(swap_places(["н", "л", "о", "с"]))
## ['с', 'л', 'о', 'н']

print("#" * 40, "Task 4", "#" * 40)


def equalize_lengths(lst):
    max_len = max([len(i) for i in lst])
    sorted_lst = sorted(lst, key=len, reverse=True)
    return [i.ljust(max_len, "_") for i in sorted_lst]


ic(equalize_lengths(["крот", "белка", "выхухоль"]))
# ['выхухоль', 'белка___', 'крот____']

ic(equalize_lengths(["a", "aa", "aaa", "aaaa", "aaaaa"]))
# ['aaaaa', 'aaaa_', 'aaa__', 'aa___', 'a____']

ic(equalize_lengths(["qweasdqweas", "q", "rteww", "ewqqqqq"]))
# ['qweasdqweas', 'ewqqqqq____', 'rteww______', 'q__________']
