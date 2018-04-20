def calculate_change(payment, cost):
    change = payment - cost
    fifty_th_count = int(change / 50000)
    print("50000::", fifty_th_count)
    change %= (fifty_th_count * 50000)
    print("rest::", change)
    ten_th_count = int(change / 10000)
    print("10000::", ten_th_count)
    change %= (ten_th_count * 10000)
    print("rest::", change)
    five_th_count = int(change / 5000)
    print("5000::", five_th_count)
    change %= (five_th_count * 5000)
    print("rest::", change)
    one_th_count = int(change / 1000)
    print("1000::", one_th_count)
    change %= (one_th_count * 1000)
    print("rest::", change)

payment = int(input("payment?: "))
cost = int(input("cost?: "))

calculate_change(payment, cost)