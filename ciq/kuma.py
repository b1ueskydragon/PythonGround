'''
https://codeiq.jp/challenge/3412
'''

# 1データに対する一日の利益
def order(income, period):
    one_day_income = income/period
    return one_day_income

test = [9, 12, 20, 23, 27]

stay = 100


def read_file():
    open_path = "sample.txt"
    data_list = []
    file = open(open_path, "r", encoding="UTF-8")

    for line in file:
        data_list.append(line[:-1].split(","))

    file.close()
    return data_list

print(read_file())


