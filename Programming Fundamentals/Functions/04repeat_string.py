# Write a function that receives a string and a counter n. The function should return a new string – the result of repeating the old string n times. 


string_input = input()
counter_n = int(input())

def new_string(string, n):
    result = string * n
    return result
print(new_string(string_input, counter_n))
