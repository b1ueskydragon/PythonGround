def spliter(log=input()):
    return log.split('\t')


log_ary = spliter()

for i, v in enumerate(log_ary):
    id = "[" + str(i) + "]"
    print(id, v)
