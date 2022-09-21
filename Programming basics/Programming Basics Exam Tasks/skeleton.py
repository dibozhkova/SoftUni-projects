min_control = int(input())
sec_control = int(input())
chute_lenght_m = float(input())
sec_for_100m = int(input())
control_sec = min_control * 60 + sec_control
reduse_time = chute_lenght_m / 120
total_reduse_time = reduse_time * 2.5
marins_time = (chute_lenght_m / 100) * sec_for_100m - total_reduse_time
if marins_time <= control_sec:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marins_time:.3f}.")
if marins_time > control_sec:
    print(f"No, Marin failed! He was {marins_time - control_sec:.3f} second slower.")
