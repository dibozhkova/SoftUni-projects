vehicles = input().split(">>")
total_collected_tax = 0
for current_vehicles in vehicles:
    current_vehicles = current_vehicles.split()
    car_type = current_vehicles[0]
    year_used = int(current_vehicles[1])
    km_traveled = int(current_vehicles[2])
    if car_type == "family":
        initial_tax = 50 - (year_used * 5) + (km_traveled // 3000 * 12)
        total_collected_tax += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        initial_tax = 80 - (year_used * 8) + (km_traveled // 9000 * 14)
        total_collected_tax += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    elif car_type == "sports":
        initial_tax = 100 - (year_used * 9) + (km_traveled // 2000 * 18)
        total_collected_tax += initial_tax
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_collected_tax:.2f} euros in taxes.")
