# これが
msg = "さたしべすにせいそこすうし"
msg = msg[1::2] + msg[::2]
print(msg)

# こうなる
msg = (lambda msg: msg[1::2] + msg[::2])
print(msg("さたしべすにせいそこすうし"))

print((lambda txt: txt[::-1][::2] + txt[1::2])(" -G_M-O"))

kbd = "新しいキーボードが届いたので試します。文字数は偶数なのかな?"
print((lambda kbd: len(kbd) % 2 == 0)(kbd))

'''
以下、参考しましたー
http://www.sejuku.net/blog/23677
'''


# lambda式を使わずに通常の関数を用いる場合
def func(price, tax):
    return price + (price * tax)


payment1 = func(100, 0.08)
print(payment1)

# lambda式を用いる場合
payment2 = (lambda price, tax: price + (price * tax))(100, 0.08)
print(payment2)
