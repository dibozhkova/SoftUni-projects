integers = [int(i) for i in input().split()]
command = input().split()
while command[0] != "end":
    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        integers[index1], integers[index2] = integers[index2], integers[index1]
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        integers[index1] *= integers[index2]
    elif command[0] == "decrease":
        integers = [el - 1 for el in integers]

    command = input().split()
print(*integers, sep=", ")


# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# •	"swap {index1} {index2}" takes two elements and swap their places.
# •	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index.
# •	"decrease" decreases all elements in the array with 1.
# Input
# On the first input line, you will be given the initial array values separated by a single space.
# On the next lines you will receive commands until you receive the command "end". The commands are as follow: 
# •	"swap {index1} {index2}"
# •	"multiply {index1} {index2}"
# •	"decrease"
# Output
# The output should be printed on the console and consist of elements of the modified array – separated by a comma and a single space ", ".
# Constraints
# •	Elements of the array will be integer numbers in the range [-231...231]
# •	Count of the array elements will be in the range [2...100]
# •	Indexes will be always in the range of the array
