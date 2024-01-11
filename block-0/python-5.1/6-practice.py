from icecream import ic

print("#" * 100)
print("Practice")
print("#" * 100)


def is_prime(num):
    if -1 <= num <= 1:
        return False
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


ic(is_prime(1))
ic(is_prime(10))
ic(is_prime(13))


print("#" * 40)

between_min_max = lambda *args: (min(args) + max(args)) / 2
ic(between_min_max(10))
ic(between_min_max(1, 2, 3, 4, 5))

print("#" * 40)


def best_student(**kwargs):
    res = list(kwargs.items())
    res.sort(key=lambda x: x[1])
    return res[0][0]


ic(best_student(Tom=12, Mike=3))
ic(best_student(Tom=12))
ic(best_student(Tom=12, Jerry=1, Jane=2))

print("#" * 40)
is_palindrom = lambda x: "yes" if [*x] == [*x][::-1] else "no"
ic(is_palindrom("1234"))
ic(is_palindrom("12321"))

print("#" * 40)
area = lambda a, b: a * b
ic(area(12, 5))
# 60

print("#" * 40)


def sort_ignore_case(ls):
    ls.sort(key=lambda str: str.lower())
    return ls


ic(sort_ignore_case(["Acc", "abc"]))
# ['abc', 'Acc']

print("#" * 40)


def exchange(**kwargs):
    if len(kwargs) < 2:
        raise ValueError("Not enough arguments")
    if len(kwargs) > 2:
        raise ValueError("Too many arguments")
    if "usd" in kwargs and "rate" in kwargs:
        return kwargs["usd"] * kwargs["rate"]
    elif "rub" in kwargs and "rate" in kwargs:
        return kwargs["rub"] / kwargs["rate"]
    elif "usd" in kwargs and "rub" in kwargs:
        return kwargs["rub"] / kwargs["usd"]


ic(exchange(usd=100, rub=8500))
# 85.0

ic(exchange(usd=100, rate=85))
# 8500

ic(exchange(rub=1000, rate=85))
# 11.764705882352942

# ic(exchange(rub=1000, rate=85, usd=90))
# ValueError: Too many arguments

# ic(exchange(rub=1000))
# ValueError: Not enough arguments
