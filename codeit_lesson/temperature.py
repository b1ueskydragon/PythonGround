
class SAMPLE:
    def __init__(self):
        self.temp_list = [40, 15, 32, 64, -4, 11]


# lambda で表現
temp_list = SAMPLE().temp_list
new_temp_list = list(map(lambda T: round((T - 32) * 5 / 9, 2), temp_list))

print("C: " + str(temp_list))
print("F: " + str(new_temp_list))


# while で表現
def temperature(T):
    return round((T - 32) * 5 / 9, 2)

i = 0
temp_list = SAMPLE().temp_list
new_temp_list = []
while i < len(temp_list):
    new_temp_list += [temperature(temp_list[i])]
    i += 1

print("C: " + str(temp_list))
print("F: " + str(new_temp_list))
