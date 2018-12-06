import random

it = list(range(10))
random.shuffle(it)
print(it)

it_ = random.sample(list(range(10)), k=10)
print(it_)


def random_(k, acc=[], memo=set()):
    while len(memo) < k:
        i = random.randrange(0, k)
        while i in memo:
            i = random.randrange(0, k)

        acc.append(i)
        memo.add(i)

    return acc


print(random_(k=10))


def random__(k, memo=set()):
    while len(memo) < k:
        i = random.randrange(0, k)
        memo.add(i)
    return memo


print(random__(k=10))
