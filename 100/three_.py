b='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
import curses.ascii as a
r=list(map(lambda x:len(list(filter(a.isalpha,x))), b.split()))  # java の map とは違う

print(r)
