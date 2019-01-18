def word_bi_gram(msg):
    a = iter(msg.split())
    b = iter(msg.split())
    next(b)
    print(list(zip(a, b)))


def char_bi_gram(stc):
    print([(stc[i - 1], stc[i]) for i in range(1, len(stc))])


given = "I am an NLPer"

word_bi_gram(given)
char_bi_gram(given)

# TODO n_gram with param n
