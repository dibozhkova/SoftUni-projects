# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.


def perfect_number(some_num):
    positive_divisors = []
    for number in range(1, some_num + 1):
        if some_num % number == 0:
            positive_divisors.append(number)
    positive_divisors = positive_divisors[:-1]
    if sum(positive_divisors) == some_num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

some_number = int(input())
perfect_number(some_number)
