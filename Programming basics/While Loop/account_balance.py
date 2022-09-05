current_sum = input()

total_sum = 0
while current_sum != "NoMoreMoney":
    copy_current_sum = float(current_sum)
    if copy_current_sum < 0:
        print("Invalid operation!")
        break
    total_sum = total_sum + copy_current_sum
    print(f"Increase: {copy_current_sum:.2f}")
    current_sum = input()
print(f"Total: {total_sum:.2f}")
