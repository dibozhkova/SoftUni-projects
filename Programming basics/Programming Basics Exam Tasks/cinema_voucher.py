sum_voucher = int(input())
line_input = input()
count_ticket = 0
count_purchase = 0
copy_sum_voucher = sum_voucher
while line_input != "End":
    purchase = line_input
    len_word = len(purchase)
    first_letter = purchase[0]
    second_letter = purchase[1]
    value_first_letter = ord(first_letter)
    value_second_letter = ord(second_letter)
    current_value = 0
    if len_word > 8:
        current_value = value_first_letter + value_second_letter
        if current_value <= copy_sum_voucher:
            copy_sum_voucher -= value_first_letter + value_second_letter
            count_ticket += 1
        else:
            break
    elif len_word <= 8:
        current_value = value_first_letter
        if current_value <= copy_sum_voucher:
            copy_sum_voucher -= value_first_letter
            count_purchase += 1
        else:
            break

    line_input = input()
print(f"{count_ticket}")
print(f"{count_purchase}")
