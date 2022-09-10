degrees = float(input())
if degrees == 5:
    print("Cold")
elif degrees <= 11.9:
    print("Cold")
elif degrees == 12:
    print("Cool")
elif degrees <= 14.9:
    print("Cool")
elif degrees == 15:
    print("Mild")
elif degrees <= 20:
    print("Mild")
elif degrees == 20.1:
    print("Warm")
elif degrees <= 25.9:
    print("Warm")
elif degrees == 26:
    print("Hot")
elif degrees <= 35:
    print("Hot")
else:
    print("unknown")
