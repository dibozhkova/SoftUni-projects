width_cake = int(input())
length_cake = int(input())

cake_pieces = width_cake * length_cake
input_line = input()
while input_line != "STOP":
    num_pieces = int(input_line)
    cake_pieces = cake_pieces - num_pieces

    if cake_pieces <= 0:
        break

    input_line = input()
diff = abs(cake_pieces)
if input_line == "STOP":
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
