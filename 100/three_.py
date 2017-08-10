b='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
import curses.ascii as a  # ASCII コード
r=list(map(lambda x:len(list(filter(a.isalpha,x))), b.split()))  # java の map とは違う

print(r)

import re  # 正規表現
pattern = r"[a-zA-Z ]"
repatter = re.compile(pattern)

basestr = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
wordsstr = "".join(repatter.findall(basestr))

wordslist = re.split(" ", wordsstr)
for word in wordslist:
    print(f"{word} : {len(word)}")
