print("Hello World!")
lie: bool = False
print(id(lie))
print(round(11 * 2.5 / 3, 2))
print(round(3.1415926**2 / 2))
print(1.57 * 3 / 1.5 == 3.14)
print(3**3 - 3 * (6 * 3 - 4.5 * 2) == 1)
# print(type())
obj = {"a": 1, "b": 2}
print(type(obj))
not_lie = bool(1)
print(not_lie)
my_list = list(range(1, 10))
print(my_list)
not_true = bool(0)

# Lists and Tuples
a = ["a", "b", "c", "d", "e"]
print(a[0:4:2])
c = list(range(-5, 5))
print(c[4:9])
b = list(range(-3, 6))
print(b[::-1])
str = "hello kitty"
print(str.split()[:2])

print("#" * 10)
a1 = "order1"
b1 = "order2"
c1 = "order3"
orders = list()
orders.append(a1)
orders.append(b1)
orders.append(c1)
print(orders)

print("#" * 10)
book1 = "my book"
book2 = "your book"
books = ["all_books"]
books.append(book1)
books.append(book2)
print(books)

print("#" * 10)
my_books = ["book1", "book2", "book3", "book4", "book5"]
tom_books = my_books.copy()
print(tom_books, my_books)

my_orders = ["order1", "order2", "order3", "order4", "order5"]
anne_orders = my_orders[:]
print(anne_orders, my_orders)

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
print(all_things)

print("#" * 10)
nums = list(range(1, 11))
nums.reverse()
print(nums)

print("#" * 10)
random_values = [3, 5, 0, -1, 2, 10, 15, -5]
random_values.sort()
print(random_values)

print("#" * 10)
list1 = [5, 0.2, "hello there", list(range(1, 5)), "bye"]
print(list1)

print("#" * 10)
# Tuples
a = (1, 2, 3, 4, 5, 6)
# создадим кортеж
b = [1, 2, 3, 4, 5, 6]
# создадим список с теми же элементами, что в кортеже выше
print(a.__sizeof__())
# 72
print(b.__sizeof__())
# 88
