follow_lines = int(input())
capacity_water_tank = 255
lt_in_tank = 0
for i in range(follow_lines):
    current_lt = int(input())
    if capacity_water_tank - current_lt < 0:
        print(f"Insufficient capacity!")
        continue
    capacity_water_tank -= current_lt
    lt_in_tank += current_lt
print(f"{lt_in_tank}")
