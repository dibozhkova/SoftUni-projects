start_eggs = int(input())

copy_start_eggs = start_eggs
sold_eggs = 0
end_eggs = False
line_input = input()
while line_input != "Close":
    command = line_input
    num_eggs = int(input())
    if command == "Fill":
        copy_start_eggs += num_eggs
    if num_eggs > copy_start_eggs:
        end_eggs = True
        break
    if command == "Buy":
        sold_eggs += num_eggs
        copy_start_eggs -= num_eggs

    line_input = input()

if line_input == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
if end_eggs:
    print("Not enough eggs in store!")
    print(f"You can buy only {copy_start_eggs}.")
