def solve(msg):
    import re

    p = re.compile(r"[a-zA-Z ]")  # only alpha and space
    xs = ''.join(p.findall(msg)).split()
    print([len(x) for x in xs])  # 3.14...


def solve_(msg):
    import curses.ascii as a  # ASCII
    print(list(map(lambda x: len(list(filter(a.isalpha, x))), msg.split())))


given = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
solve(given)
solve_(given)
