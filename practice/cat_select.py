import random as rd

cat_list = ["なる", "とき"]
select_list = []


def cat_select():
    for i in range(10000):
        select_list.append(cat_list[rd.randrange(2)])

    naru = 0
    toki = 0

    for c in select_list:
        if c == cat_list[0]:
            naru += 1
        else:
            toki += 1

    return "naru: " + str(naru) + " toki: " + str(toki)


print(cat_select())
