
serial = input()
seasons = int(input())
episodes = int(input())
time_episod = float(input())
advertisement = time_episod * 0.2
total_min = (episodes * time_episod * seasons) + (episodes * advertisement * seasons) + (seasons * 10)
print(f"Total time needed to watch the {serial} series is {round(total_min)} minutes.")
