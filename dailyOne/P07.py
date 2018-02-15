def count_decode(msg):
    s = set()

    count = 1

    parseMsg = int(msg)
    if parseMsg < 11: return 1
    if parseMsg < 27: return 2

    for i in range(len(msg)):
        pair = msg[i:i + 2]
        parsedPair = int(pair)

        if parsedPair < 27:
            s.add(pair)

    return count + len(s)


print(count_decode('128'))
