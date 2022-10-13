# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...). 
# Your task is to create a function that returns a loading bar depending on the number you have received in the input. 
# Print the result on the console. For more clarification, see the examples below.


def loading_bar(number):
    ready = ("%" * int(number / 10))
    remain = ("." * int(10 - number / 10))
    load_bar = ready + remain
    return load_bar

num = int(input())
if num == 100:
    print(f'100% Complete!\n[{loading_bar(num)}]')
else:
    print(f'{num}% [{loading_bar(num)}]\nStill loading...')
