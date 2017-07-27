def one() :
    target = "パタトクカシーー"
    new_target = ""

    for i in range(len(target)):
        if i % 2 != 0:
            new_target += target[i]
    return new_target

print(one())