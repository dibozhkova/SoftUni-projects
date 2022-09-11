holidays = int(input())
play_time_holidays = holidays * 127
work_play = (365 - holidays) * 63
all_time_play = play_time_holidays + work_play
rest = abs(30000 - all_time_play)
hours = rest // 60
minutes = rest % 60
if all_time_play < 30000:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{abs(hours)} hours and {abs(minutes)} minutes more for play")
