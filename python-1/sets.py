from icecream import ic

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
