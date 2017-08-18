temp_list = [40, 15, 32, 64, -4, 11]
new_temp_list = list(map(lambda T: round((T - 32) * 5 / 9, 2), temp_list))

print("C: " + str(temp_list))
print("F: " + str(new_temp_list))