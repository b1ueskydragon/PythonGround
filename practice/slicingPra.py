moji = "abcd"

print(moji[1:4])

print(moji[1:4:2])

print(moji[1::])

print(moji[::2])

print(moji[::1])

print(moji[::])

print(moji[::-1])  # dcba

print(moji[-1::-1])  # dcba

print(moji[1::-1])

print(moji[3::-1])  # dcba

print("あ")
print(moji[5::-1])  # dcba

print("い")
print(moji[3:0:-1])  # dcba

print("う")
print(moji[-1::1])

print("実はbuilt-in-function")
print(type(slice(moji)))

'''start idx : stop idx : step '''
''' -1 = 末尾'''
''' start idx <= [//] < stop idx '''

apply = "かあくりさがんと、う|ご|ざ|い|ま|す"

print(apply[::2].replace("|", " :D ") + apply[::-2][::-1])
