fuel_type = input()
fuel_available = float(input())
if fuel_type == "Diesel":
    if fuel_available >= 25:
        print("You have enough diesel.")
    elif fuel_available < 25:
        print("Fill your tank with diesel!")
elif fuel_type == "Gasoline":
    if fuel_available >= 25:
        print("You have enough gasoline.")
    elif fuel_available < 25:
        print("Fill your tank with gasoline!")
elif fuel_type == "Gas":
    if fuel_available >= 25:
        print("You have enough gas.")
    elif fuel_available < 25:
        print("Fill your tank with gas!")
else:
    print("Invalid fuel!")
