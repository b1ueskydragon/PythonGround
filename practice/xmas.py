import re

msg = 'Merry-Christmas'
pattern = r"[a-zA-Z ]"

ints = [ord(s) for s in msg if re.match(pattern, s)]

print(ints)
print(''.join(list(map(lambda s: chr(s), ints))))
