S = "a1b2c3d4efg567hi"
alphas_a = [[s.lower(), s.upper()] if s.isalpha() else s for s in S]
alphas_b = [s if "0" <= s <= "9" else [s.lower(), s.upper()] for s in S]

print(alphas_a)
print(alphas_b)
assert (alphas_a == alphas_b)
