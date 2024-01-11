from icecream import ic

print("#" * 100)
print("Sets")
print("#" * 100)
s = set("hello")
ic(s)
# {'h', 'e', 'l', 'o'}

print("#" * 40)
s1 = set()
ic(s)
# set()

print("#" * 40)
s2 = {5, 10, 3, 2, 11}
ic(s2)
# {2, 3, 5, 10, 11}

print("#" * 40)
s3 = set("wow thats cool")
ic(s3)
# {'a', ' ', 'c', 'h', 'l', 'o', 's', 't', 'w'}

print("#" * 40, "add", "#" * 40)
s1 = set("abcde")
s1.add("hello")
ic(s1)
# {'c', 'a', 'd', 'hello', 'e', 'b'}

print("#" * 40, "update", "#" * 40)
s1 = set("abcde")
s1.update("hello")
ic(s1)
# {'c', 'a', 'd', 'l', 'o', 'e', 'h', 'b'}

print("#" * 40, "remove", "#" * 40)
s1 = set("abcde")
s1.remove("d")
ic(s1)
# {'c', 'a', 'e', 'b'}

print("#" * 40, "discard", "#" * 40)
s1 = set("abcdef")
s1.discard("f")
ic(s1)
# {'c', 'a', 'e', 'b', 'd'}

print("#" * 40)
s1 = set("abcdef")
s1.remove("f")
s1
ic(s1)
# {'a', 'b', 'c', 'd', 'e'}

print("#" * 40, "union", "#" * 40)
cluster1 = {"item1", "item2", "item3", "item4"}
cluster2 = {"item2", "item3", "item5", "item7"}
ic(cluster1.union(cluster2))
# {"item1", "item2", "item3", "item4", "item5", "item7"}

print("#" * 40)
alpha_set = set("abcde")
name = set("bad boy")
ic(alpha_set.union(name))
# {'o', 'e', 'a', 'b', 'y', 'c', 'd', ' '}

print("#" * 40)
num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
date_num = set([1, 9, 4, 8])
ic(num_set.union(date_num))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("#" * 40, "intersection", "#" * 40)
cluster1 = {"item1", "item2", "item3", "item4"}
cluster2 = {"item2", "item3", "item5", "item7"}
ic(cluster1.intersection(cluster2))
# {"item2", "item3"}

print("#" * 40)
alpha_set = set("abcde")
name = set("bad boy")
ic(alpha_set.intersection(name))
# {'a', 'b', 'd'}

print("#" * 40)
num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
date_num = set([1, 9, 4, 8])
ic(num_set.intersection(date_num))
# {1, 8, 9, 4}

print("#" * 40, "difference", "#" * 40)
cluster1 = {"item1", "item2", "item3", "item4", "item5"}
cluster2 = {"item3", "item4", "item5", "item6"}
ic(cluster1.difference(cluster2))
# {"item1", "item2"}

print("#" * 40)
alpha_set = set("abcde")
name = "bad boy"
ic(alpha_set.difference(name))
# {'c', 'e'}

print("#" * 40)
num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
date_num = set([1, 9, 4, 8])
ic(num_set.difference(date_num))
# {0, 2, 3, 5, 6, 7, 10}

print("#" * 40, "issubset", "#" * 40)
cluster1 = {"item1", "item2", "item3"}
cluster2 = {"item2", "item3", "item4", "item5", "item6"}
ic(cluster1.issubset(cluster2))
# False

print("#" * 40)
alpha_set = set("abcde")
beta_set = set("abc")
ic(beta_set.issubset(alpha_set))
# True
