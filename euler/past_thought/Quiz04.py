#coding: UTF-8
'''
10,001番目の素数を求めるプログラムを作成せよ。
'''

def findPrimeNum(rng, idx):
    # Listのnew
    primeNumList = []
    primeNumList.append(2)

    for i in range (rng):
        for j in range (2, i):
            if i not in primeNumList:
                primeNumList.append(i)
            if (i % j) == 0:
                primeNumList.remove(i)
                break

    return primeNumList[idx]


print(findPrimeNum(100000 , 10000))