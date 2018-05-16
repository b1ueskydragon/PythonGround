msg = "さたしべすにせいそこすうし"
msg = msg[1::2] + msg[::2]
print(msg)

msg = (lambda msg: msg[1::2] + msg[::2])
print(msg("さたしべすにせいそこすうし"))

print((lambda txt: txt[::-1][::2] + txt[1::2])(" -v_v-v"))

kbd = "新しいキーボードが届いたので試します。文字数は偶数なのかな?"
print((lambda kbd: len(kbd) % 2 == 0)(kbd))


def func(price, tax):
    return price + (price * tax)


payment1 = func(100, 0.08)
print(payment1)

payment2 = (lambda price, tax: price + (price * tax))(100, 0.08)
print(payment2)

xy = [[3, 5, 1], [4, 2, 9]]
ans = list(map(lambda x, y: x ** 2 + y, *xy))
print(ans)
