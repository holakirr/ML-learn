list1 = list()
list1.append(1)
list1.append(2)
list1.append(3)
print(list1)

list2 = range(-5, 15, 2)
list3 = [
    1,
    2,
    3,
    4,
]
list3.extend(list2)
print(list3)

list6 = [3, 1, -10, 5, 11, 20, 1, -10]
list7 = list6.copy()
list6.sort()
list_result = list6
list_result.reverse()
print(list7, list_result)

list1 = [10, 15]
tpl1 = tuple(list1)
dict1 = {tpl1: "Hello"}
print(dict1)

dict1 = {"name": "unknown"}
dict2 = {"name": "Tom"}
print(dict1, dict2, dict.keys(dict1), dict.values(dict1))

s1 = set("hello")
s2 = ["w", "o", "w"]
print(s1.union(s2), s1.intersection(s2), s1.difference(s2))

result = "age is " + str(15)
print(result)
