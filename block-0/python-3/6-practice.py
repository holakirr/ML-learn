from icecream import ic

print("#" * 100)
print("Practice")
print("#" * 100)

print(
    "#" * 40,
    "Using logical and comparison operators in a conditional statement",
    "#" * 40,
)
# не лучший способ
month = 1
if month == 3 or month == 4 or month == 5:
    ic("Spring")
# хорошо
if month in [3, 4, 5]:
    ic("Spring")

print("#" * 40)
if month in [3, 4, 5]:  # весна
    ic("Spring")
elif month in [6, 7, 8]:  # лето
    ic("Summer")
elif month in [9, 10, 11]:  # осень
    ic("Autumn")
elif month in [12, 1, 2]:  # зима
    ic("Winter")
else:  # некорректный номер месяца
    ic("Incorrect month number")

print("#" * 40, "Complex tasks", "#" * 40)

print("#" * 40)
dish_time_dict = {
    "Рамен с говядиной": 15,
    "Суши": 18,
    "Лагман с курицей": 20,
    "Лагман с говядиной": 24,
    "Плов с курицей": 28,
}
street_time_dict = {
    "Дзержинский": 39,
    "Солнечный": 40,
    "Заводской": 27,
    "Гагаринский": 43,
    "Кировский": 37,
    "Октябрьский": 34,
}
dish, street = "Рамен с говядиной", "Заводской"
street = "Заводской"
ic(street not in street_time_dict)
# True
if street not in street_time_dict:
    ic("Доставка в ваш район недоступна")
elif dish not in dish_time_dict:
    ic("Блюдо недоступно, закажите что-то другое")
else:
    # здесь будет дальнейший код
    print()

dish_time = dish_time_dict[dish]  # время приготовления блюда
street_time = street_time_dict[street]  # время доставки
full_time = dish_time + street_time  # общее время доставки
delay = full_time - 60  # задержка
if delay <= 0:
    # задержка не положительна
    ic("Заказ будет доставлен вовремя")
else:
    # задержка положительная
    ic("Курьер задержится на {} минут".format(delay))

if street not in street_time_dict:
    # неизвестный район
    ic("Доставка в ваш район недоступна")
elif dish not in dish_time_dict:
    # неизвестное блюдо
    ic("Блюдо недоступно, закажите что-то другое")
else:
    # район доступен для доставки и блюдо известно
    dish_time = dish_time_dict[dish]  # время приготовления блюда
    street_time = street_time_dict[street]  # время доставки
    full_time = dish_time + street_time  # общее время доставки
    delay = full_time - 60  # задержка
    if delay <= 0:
        # задержка не положительна
        ic("Заказ будет доставлен вовремя")
    else:
        # задержка положительная
        ic("Курьер задержится на {} минут".format(delay))

dish, street = "Рамен с говядиной", "Заводской"
# Заказ будет доставлен вовремя

dish, street = "Плов с курицей", "Солнечный"
# "Курьер задержится на 8 минут"

dish, street = "Бургер с говядиной", "Солнечный"
# "Блюдо недоступно, закажите что-то другое"

print("#" * 40)
purchases = ["Adidas", "Nike"]
prices = {"Adidas": 4298, "Nike": 6550, "Puma": 4490, "Asics": 3879}
sale = 5
result_str = "Стоимость заказа составила: {}"
price = None
total = None

if not purchases:
    ic("Ваша корзина пуста")
elif len(purchases) == 1:
    price = prices[purchases[0]]
    ic(result_str.format(price))
else:
    result_str = "Стоимость заказа составила: {}. С учетом скидки в {}% — {}"
    if purchases[0] == purchases[1]:
        sale = 10
    price = prices[purchases[0]] + prices[purchases[1]]
    total = (100 - sale) / 100 * price
    ic(result_str.format(price, sale, total))
