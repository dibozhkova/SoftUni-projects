import math

record = float(input())
distance_in_m = float(input())
time_in_sec_for_1m = float(input())

time_climbing = distance_in_m * time_in_sec_for_1m
delay = math.floor((distance_in_m / 50)) * 30
total_time_climbing = time_climbing + delay

if total_time_climbing < record:
    print(f"Yes! The new record is {total_time_climbing:.2f} seconds.")
else:
    diff = total_time_climbing - record
    print(f"No! He was {diff:.2f} seconds slower.")
