from icecream import ic

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
