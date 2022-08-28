record_sec = float(input())
distance_m = float(input())
time_in_sec_for_m = float(input())
total_sec = distance_m * time_in_sec_for_m
resistance_sec = (distance_m // 15) * 12.5
final_sec = total_sec + resistance_sec
if final_sec < record_sec:
    print(f" Yes, he succeeded! The new world record is {final_sec:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record_sec - final_sec):.2f} seconds slower.")
# решена самостоятелно, като първият път имах грешка / elif вместо else/