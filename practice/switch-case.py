import re

my_tuple = (
    ("t1", "path1"),
    ("t2", "path2"),
    ("t3", "path3"),
    ("t4", "path4")
)

my_func = lambda s: next(v for k, v in my_tuple if re.match(k, s))

print(my_func("t1"))
print(my_func("t3"))

my_dict = {
    "a": "A",
    "b": "B"
}

simple_func = lambda k: my_dict[k]

print(simple_func("b"))

print(my_dict["a"])
