some_string = input()
string_in_list = some_string.split()
opposite_list = []
for element in string_in_list:
    opposite_list.append(-int(element))
print(opposite_list)
