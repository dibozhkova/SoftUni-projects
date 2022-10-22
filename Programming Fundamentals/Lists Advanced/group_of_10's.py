# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.


list_of_numbers = [int(num) for num in input().split(", ")]
group = 0
while len(list_of_numbers) > 0:
    group += 10
    new_list = []
    for num in list_of_numbers:
        if num <= group:
            new_list.append(num)
    list_of_numbers = [i for i in list_of_numbers if i not in new_list]
    print(f"Group of {group}'s: {new_list}")
