# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".


def data_types(string, value):
    surround_symbol = "$"
    if string == "int":
        value = int(value) * 2
        print(value)
    elif string == "real":
        value = float(value) * 1.5
        print(f"{value:.2f}")
    elif string == "string":
        value = surround_symbol + value + surround_symbol
        print(value)

some_string = input()
some_value = input()
data_types(some_string, some_value)
