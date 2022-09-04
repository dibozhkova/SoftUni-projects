name = input()
user_pass = input()
current_pass = input()
while current_pass != user_pass:
    current_pass = input()
print(f"Welcome {name}!")
