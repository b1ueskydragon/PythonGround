# sample
import re

r = re.compile("([a-zA-Z]+)([0-9]+)")
strings = ['foofo21', 'bar432', 'foobar12345']
print([r.match(string).groups() for string in strings])
