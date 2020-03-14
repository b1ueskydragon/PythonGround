"""
How can we fix the anonymous functions to behave as we'd expect?
"""
functions = []
for i in range(10):
    functions.append(lambda i: i)  # create local i

for i, f in enumerate(functions):
    print(f(i))  # pass i from outside
