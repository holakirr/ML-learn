from icecream import ic

print("#" * 100)
print("Practice")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)


## Введите свое решение ниже
def filter_by_fat(cheese_data, n):
    res = {}
    for cheese in cheese_data:
        if cheese_data[cheese][2] < n:
            res[cheese] = cheese_data[cheese][2]
    return res


cheese_data = {
    "чеддер": [370, 5000, 33, "твердый"],
    "пармезан": [510, 4000, 29, "твердый"],
    "гауда": [250, 3700, 27, "полутвердый"],
    "эдам": [220, 10000, 30, "полутвердый"],
    "горгонзола": [320, 3000, 32, "полумягкий"],
    "рокфор": [340, 15000, 31, "полумягкий"],
    "стилтон": [360, 7000, 35, "полумягкий"],
    "камамбер": [250, 8000, 24, "мягкий"],
    "бри": [310, 6500, 28, "мягкий"],
}
ic(filter_by_fat(cheese_data, 30))

print("#" * 40, "Task 2", "#" * 40)


def count_money(cheese_data):
    res = 0
    for cheese in cheese_data:
        res += cheese_data[cheese][0] * cheese_data[cheese][1]
    return res * 10


ic(count_money(cheese_data))

print("#" * 40, "Task 3", "#" * 40)


def find_cheese_type(cheese_data, cheese_type):
    res = []
    for cheese in cheese_data:
        if cheese_data[cheese][3] == cheese_type:
            res.append(cheese)
    return res


ic(find_cheese_type(cheese_data, "твердый"))

print("#" * 40, "Task 4", "#" * 40)


def sort_cheese(cheese_data):
    return sorted(cheese_data, key=lambda a: cheese_data[a][0])


ic(sort_cheese(cheese_data))

print("#" * 40, "Task 5", "#" * 40)


def purchase(ingredients):
    res = {}
    any_repeat = False
    for ingredient in ingredients:
        if ingredient in res:
            res[ingredient] += 1
        else:
            res[ingredient] = 1
    for ingredient in res:
        if res[ingredient] > 1:
            any_repeat = True
            ic(
                f"Вы продублировали ингредиент {ingredient} в заказе {res[ingredient]} раз(а)"
            )
    if not any_repeat:
        ic("Ваш заказ оформлен верно")


ingredients = [
    "кислота уксусная",
    "кислота лимонная",
    "закваска",
    "кислота молочная",
    "пряность",
    "бактерии",
    "аннато",
    "кальций",
    "калий",
    "специя",
    "молоко коровье",
    "молоко овечье",
    "фермент",
    "соль",
    "сливки",
    "грибки",
    "ароматизатор",
    "молоко козье",
    "дрожжи",
    "каротин",
]

purchase(ingredients)
# Ваш заказ оформлен верно

ingredients = [
    "молоко коровье",
    "молоко овечье",
    "бактерии",
    "молоко козье",
    "сливки",
    "фермент",
    "закваска",
    "молоко коровье",
    "соль",
    "молоко коровье",
    "бактерии",
    "молоко овечье",
    "кислота лимонная",
    "грибки",
    "соль",
    "дрожжи",
    "кислота уксусная",
    "кальций",
    "калий",
    "каротин",
    "аннато",
    "специя",
    "пряность",
    "ароматизатор",
    "соль",
    "кислота молочная",
]

purchase(ingredients)
# Вы продублировали ингредиент бактерии в заказе 2 раз(а)
# Вы продублировали ингредиент молоко коровье в заказе 3 раз(а)
# Вы продублировали ингредиент молоко овечье в заказе 2 раз(а)
# Вы продублировали ингредиент соль в заказе 3 раз(а)
