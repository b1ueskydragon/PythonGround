"""
What does the below code snippet print out?
"""
functions = []
for i in range(10):
    functions.append(lambda: i)

for f in functions:
    print(f())
