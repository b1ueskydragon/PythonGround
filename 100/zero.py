def zero():

    target = "stressed"
    target_list = []

    for i in range(len(target)):
        target_list.append(target[i])

    for i in range(int(len(target_list)/2)):
        target_list[i], target_list[len(target_list) - 1 - i] = target_list[len(target_list) - 1 - i], target_list[i]

    target = ""
    for i in range(len(target_list)):
        target += target_list[i]

    return target

print(zero())

