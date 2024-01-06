from icecream import ic

ic("Hello World!")
lie: bool = False
ic(id(lie))
ic(round(11 * 2.5 / 3, 2))
ic(round(3.1415926**2 / 2))
ic(1.57 * 3 / 1.5 == 3.14)
ic(3**3 - 3 * (6 * 3 - 4.5 * 2) == 1)
# ic(type())
obj = {"a": 1, "b": 2}
ic(type(obj))
not_lie = bool(1)
ic(not_lie)
my_list = list(range(1, 10))
ic(my_list)
not_true = bool(0)

print("#" * 100)
print("Lists and Tuples")
print("#" * 100)
a = ["a", "b", "c", "d", "e"]
ic(a[0:4:2])
c = list(range(-5, 5))
ic(c[4:9])
b = list(range(-3, 6))
ic(b[::-1])
str = "hello kitty"
ic(str.split()[:2])

print("#" * 10)
a1 = "order1"
b1 = "order2"
c1 = "order3"
orders = list()
orders.append(a1)
orders.append(b1)
orders.append(c1)
ic(orders)

print("#" * 10)
book1 = "my book"
book2 = "your book"
books = ["all_books"]
books.append(book1)
books.append(book2)
ic(books)

print("#" * 10)
my_books = ["book1", "book2", "book3", "book4", "book5"]
tom_books = my_books.copy()
ic(tom_books, my_books)

my_orders = ["order1", "order2", "order3", "order4", "order5"]
anne_orders = my_orders[:]
ic(anne_orders, my_orders)

print("#" * 10)
all_things = [
    "order1",
    "order2",
    "order3",
]
only_books = [
    "book1",
    "book2",
]
all_things.extend(only_books)
ic(all_things)

print("#" * 10)
nums = list(range(1, 11))
nums.reverse()
ic(nums)

print("#" * 10)
random_values = [3, 5, 0, -1, 2, 10, 15, -5]
random_values.sort()
ic(random_values)

print("#" * 10)
list1 = [5, 0.2, "hello there", list(range(1, 5)), "bye"]
ic(list1)

print("#" * 100)
print("Tuples")
print("#" * 100)
a = (1, 2, 3, 4, 5, 6)
# создадим кортеж
b = [1, 2, 3, 4, 5, 6]
# создадим список с теми же элементами, что в кортеже выше
ic(a.__sizeof__())
# 72
ic(b.__sizeof__())
# 88

print("#" * 100)
print("Dictionaries")
print("#" * 100)
alphabet_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
}
ic(alphabet_dict["d"])

print("#" * 10)
place_and_money = {
    1: 100,
    2: 50,
    3: 10,
}
ic(place_and_money[2])

print("#" * 10)
place_and_money[4] = 5
ic(place_and_money)

print("#" * 10)
place_and_money.pop(4)
place_and_money[3] = 25
ic(place_and_money)

print("#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
ic(place_and_money.keys())

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
ic(name_to_age.keys())

print("#" * 10)
ic(name_to_age.values())

print("#" * 10)
ic(place_and_money.values())

print("#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
ic(place_and_money.get(20, 0))

print("#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
place_and_money.update({4: 5, 5: 1})
ic(place_and_money)

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
name_to_age.update({"Anne": 23, "Phillip": 29})
ic(name_to_age)

print("#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
ic(place_and_money.pop(3))

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
ic(name_to_age.pop("Anton"))

print("#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
place_and_money.setdefault(10, 1)
ic(place_and_money)

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
name_to_age.setdefault("Anne", 32)
ic(name_to_age)

print("#" * 10)
test_dict = dict()
test_dict.setdefault(5, [3, 4, 5])
test_dict.setdefault((3, 4, 5), "strong man")
ic(test_dict)

print("#" * 10)
test_dict2 = dict()
test_dict2.setdefault("name", "Sancho")
test_dict2.setdefault("surname", "Panso")
test_dict2.setdefault("info", {"age": 35, "country": "Mexico"})
ic(test_dict2)

print("#" * 10)
test_dict3 = dict()
test_dict3.setdefault("info", [10, 15, 27])
test_dict3.setdefault("about", {"game": "football", "period": 5})
test_dict3.update({"about": "dont know"})
ic(test_dict3)
