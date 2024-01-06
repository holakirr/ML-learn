from icecream import ic

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
print(str.split()[:2])
# ['hello', 'kitty']

print("#" * 10, "append", "#" * 10)
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

print("#" * 10, "copy", "#" * 10)
my_books = ["book1", "book2", "book3", "book4", "book5"]
tom_books = my_books.copy()
ic(tom_books, my_books)
# or
my_orders = ["order1", "order2", "order3", "order4", "order5"]
anne_orders = my_orders[:]
ic(anne_orders, my_orders)

print("#" * 10, "extend", "#" * 10)
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

print("#" * 10, "reverse", "#" * 10)
nums = list(range(1, 11))
nums.reverse()
ic(nums)

print("#" * 10, "sort", "#" * 10)
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
# 4

print("#" * 10, "get", "#" * 10)
place_and_money = {
    1: 100,
    2: 50,
    3: 10,
}
ic(place_and_money[2])
# 50

print("#" * 10, "set", "#" * 10)
place_and_money = {
    1: 100,
    2: 50,
    3: 10,
}
place_and_money[4] = 5
ic(place_and_money)
# {1: 100, 2: 50, 3: 10, 4: 5}

print("#" * 10)
place_and_money = {
    1: 100,
    2: 50,
    3: 10,
}
place_and_money[3] = 25
ic(place_and_money)
# {1: 100, 2: 50, 3: 25}

print("#" * 10, "keys", "#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
ic(place_and_money.keys())
# dict_keys([1, 2, 3])

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
ic(name_to_age.keys())
# dict_keys(['Anne', 'Anton', 'Phillip'])

print("#" * 10, "values", "#" * 10)
ic(name_to_age.values())
# dict_values([22, 27, 30])

print("#" * 10)
ic(place_and_money.values())
# dict_values([100, 50, 10])

print("#" * 10, "get", "#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
ic(place_and_money.get(20, 0))
# 0

print("#" * 10, "update", "#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
place_and_money.update({4: 5, 5: 1})
ic(place_and_money)
# {1: 100, 2: 50, 3: 10, 4: 5, 5: 1}

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
name_to_age.update({"Anne": 23, "Phillip": 29})
ic(name_to_age)
# {'Anne': 23, 'Anton': 27, 'Phillip': 29}

print("#" * 10, "pop", "#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
ic(place_and_money.pop(3))
# 10

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
ic(name_to_age.pop("Anton"))
# 27

print("#" * 10, "setdefault", "#" * 10)
place_and_money = {1: 100, 2: 50, 3: 10}
place_and_money.setdefault(10, 1)
ic(place_and_money)
# {1: 100, 2: 50, 3: 10, 10: 1}

print("#" * 10)
name_to_age = {"Anne": 22, "Anton": 27, "Phillip": 30}
name_to_age.setdefault("Anne", 32)
ic(name_to_age)
# {'Anne': 22, 'Anton': 27, 'Phillip': 30}

print("#" * 10)
test_dict = dict()
test_dict.setdefault(5, [3, 4, 5])
test_dict.setdefault((3, 4, 5), "strong man")
ic(test_dict)
# {5: [3, 4, 5], (3, 4, 5): 'strong man'}

print("#" * 10)
test_dict2 = dict()
test_dict2.setdefault("name", "Sancho")
test_dict2.setdefault("surname", "Panso")
test_dict2.setdefault("info", {"age": 35, "country": "Mexico"})
ic(test_dict2)
# {'name': 'Sancho', 'surname': 'Panso', 'info': {'age': 35, 'country': 'Mexico'}}

print("#" * 10)
test_dict3 = dict()
test_dict3.setdefault("info", [10, 15, 27])
test_dict3.setdefault("about", {"game": "football", "period": 5})
test_dict3.update({"about": "dont know"})
ic(test_dict3)
# {'info': [10, 15, 27], 'about': 'dont know'}

print("#" * 100)
print("Sets")
print("#" * 100)
s = set("hello")
ic(s)
# {'h', 'e', 'l', 'o'}

print("#" * 10)
s1 = set()
ic(s)
# set()

print("#" * 10)
s2 = {5, 10, 3, 2, 11}
ic(s2)
# {2, 3, 5, 10, 11}

print("#" * 10)
s3 = set("wow thats cool")
ic(s3)
# {'a', ' ', 'c', 'h', 'l', 'o', 's', 't', 'w'}

print("#" * 10, "add", "#" * 10)
s1 = set("abcde")
s1.add("hello")
ic(s1)
# {'c', 'a', 'd', 'hello', 'e', 'b'}

print("#" * 10, "update", "#" * 10)
s1 = set("abcde")
s1.update("hello")
ic(s1)
# {'c', 'a', 'd', 'l', 'o', 'e', 'h', 'b'}

print("#" * 10, "remove", "#" * 10)
s1 = set("abcde")
s1.remove("d")
ic(s1)
# {'c', 'a', 'e', 'b'}

print("#" * 10, "discard", "#" * 10)
s1 = set("abcdef")
s1.discard("f")
ic(s1)
# {'c', 'a', 'e', 'b', 'd'}

print("#" * 10)
s1 = set("abcdef")
s1.remove("f")
s1
ic(s1)
# {'a', 'b', 'c', 'd', 'e'}

print("#" * 10, "union", "#" * 10)
cluster1 = {"item1", "item2", "item3", "item4"}
cluster2 = {"item2", "item3", "item5", "item7"}
ic(cluster1.union(cluster2))
# {"item1", "item2", "item3", "item4", "item5", "item7"}

print("#" * 10)
alpha_set = set("abcde")
name = set("bad boy")
ic(alpha_set.union(name))
# {'o', 'e', 'a', 'b', 'y', 'c', 'd', ' '}

print("#" * 10)
num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
date_num = set([1, 9, 4, 8])
ic(num_set.union(date_num))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("#" * 10, "intersection", "#" * 10)
cluster1 = {"item1", "item2", "item3", "item4"}
cluster2 = {"item2", "item3", "item5", "item7"}
ic(cluster1.intersection(cluster2))
# {"item2", "item3"}

print("#" * 10)
alpha_set = set("abcde")
name = set("bad boy")
ic(alpha_set.intersection(name))
# {'a', 'b', 'd'}

print("#" * 10)
num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
date_num = set([1, 9, 4, 8])
ic(num_set.intersection(date_num))
# {1, 8, 9, 4}

print("#" * 10, "difference", "#" * 10)
cluster1 = {"item1", "item2", "item3", "item4", "item5"}
cluster2 = {"item3", "item4", "item5", "item6"}
ic(cluster1.difference(cluster2))
# {"item1", "item2"}

print("#" * 10)
alpha_set = set("abcde")
name = "bad boy"
ic(alpha_set.difference(name))
# {'c', 'e'}

print("#" * 10)
num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
date_num = set([1, 9, 4, 8])
ic(num_set.difference(date_num))
# {0, 2, 3, 5, 6, 7, 10}

print("#" * 10, "issubset", "#" * 10)
cluster1 = {"item1", "item2", "item3"}
cluster2 = {"item2", "item3", "item4", "item5", "item6"}
ic(cluster1.issubset(cluster2))
# False

print("#" * 10)
alpha_set = set("abcde")
beta_set = set("abc")
ic(beta_set.issubset(alpha_set))
# True
