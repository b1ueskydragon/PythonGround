#coding: UTF-8
'''
10,001番目の素数を求めるプログラムを作成せよ。
'''
import time
millis_s = int(time.time() * 1000)

def findPrimeNum(rng, idx):

    targetList = []

    for i in range(rng):
        for j in range(2, i):
            if i not in targetList:
                targetList.append(i)
            if i%j == 0:
                targetList[-1] = 0
                break

    primeNumList = []
    primeNumList.append(2)

    for i in targetList.__iter__():
       if i == 0:
           continue
       primeNumList.append(i)

    return primeNumList[idx]

print("result is: ", findPrimeNum(120000, 10000))

millis_e = int(time.time() * 1000)
print(millis_e - millis_s, "")