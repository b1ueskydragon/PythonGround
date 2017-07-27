def three():
    target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    target_list = target.split(" ")

    for i in range(len(target_list)):
        if target_list[i].isalpha():
            continue
        else:
            target_list[i] = target_list[i][:len(target_list[i]) - 2]

    py = []
    for i in range(len(target_list)):
        py.append(len(target_list[i]))

    return py


print(three())
