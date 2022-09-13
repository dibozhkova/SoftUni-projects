num_cargo = int(input())

van = 0
truck = 0
train = 0

for i in range(1, num_cargo + 1):
    sum_ton = int(input())
    if sum_ton <= 3:
        van = sum_ton + van
    elif 4 <= sum_ton <= 11:
        truck = sum_ton + truck
    elif sum_ton >= 12:
        train = sum_ton + train

total_tons = van + truck + train
average_price = (van * 200 + truck * 175 + train * 120) / total_tons
print(f"{average_price:.2f}")
percent_van = (van / total_tons) * 100
print(f"{percent_van:.2f}%")
percent_truck = (truck / total_tons) * 100
print(f"{percent_truck:.2f}%")
percent_train = (train / total_tons) * 100
print(f"{percent_train:.2f}%")
