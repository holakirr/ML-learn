from icecream import ic

print("#" * 100)
print("Lists")
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
