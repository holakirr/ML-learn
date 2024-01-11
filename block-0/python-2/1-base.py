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
