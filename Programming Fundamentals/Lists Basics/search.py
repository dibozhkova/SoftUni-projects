number = int(input())
word = input()
list = []
filter_list = []
for _ in range(number):
    some_string = input()
    list.append(some_string)
    if word in some_string:
        filter_list.append(some_string)
print(list)
print(filter_list)
