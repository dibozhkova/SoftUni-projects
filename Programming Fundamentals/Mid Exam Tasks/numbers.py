integers = [int(i) for i in input().split()]
avr_value = sum(integers) / len(integers)
top_5 = []
for num in sorted(integers, reverse=True):
    if num > avr_value:
        top_5.append(num)
        if len(top_5) == 5:
            break
if len(top_5) == 0:
    print("No")
else:
    print(*top_5, sep=" ")
    
    
#     Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in the sequence, sorted in descending order.
# Input
# •	Read from the console a single line holding space-separated integers.
# Output
# •	Print the above-described numbers on a single line, space-separated. 
# •	If less than 5 numbers hold the property mentioned above, print less than 5 numbers. 
# •	Print "No" if no numbers hold the above property.
# Constraints
# •	All input numbers are integers in the range [-1 000 000 … 1 000 000]. 
# •	The count of numbers is in the range [1…10 000].
