def two():
    pat = "パトカー"
    tax = "タクシー"
    result = ""

    ele = ""
    for i in range(len(pat)):
        ele = pat[i] + tax[i]
        result += ele

    return result


print(two())
