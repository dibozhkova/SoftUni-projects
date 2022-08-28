budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

video_card_price = video_card * 250
processor_price = video_card_price * 0.35 * processor
ram_price = video_card_price * 0.1 * ram
all_sum = video_card_price + processor_price + ram_price
if video_card > processor:
    all_sum = all_sum * 0.85
if budget >= all_sum:
    print(f"You have {budget - all_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {(all_sum - budget):.2f} leva more!")
    # два пъти грешка в джъдж! да внимавам за интервалите при if/else и print

