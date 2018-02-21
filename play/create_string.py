import string, random, hashlib

print("".join(random.sample(string.printable[0:62], 8)))

print("".join(random.sample(string.printable[0:62], 22)))
print("".join(random.sample(string.printable[0:62], 22)))

print(hashlib.sha256(b"").hexdigest())
print(hashlib.sha256(b"").hexdigest())
