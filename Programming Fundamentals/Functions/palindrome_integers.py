# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ". 
# The function should check if each integer is a palindrome - True or False. Print the result.


def palindrome_numbers(num):
    for integer in num:
        reverse_integer = integer[::-1]
        if integer == reverse_integer:
            print("True")
        else:
            print("False")

list_of_integers_as_str = input().split(", ")
palindrome_numbers(list_of_integers_as_str)
