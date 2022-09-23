time_shoot = int(input())
scenes = int(input())
duration_scene = int(input())
field_preparation = time_shoot * 0.15
duration_all_scenes = scenes * duration_scene + field_preparation
if time_shoot >= duration_all_scenes:
    print(f"You managed to finish the movie on time! You have {round(time_shoot - duration_all_scenes)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(duration_all_scenes - time_shoot)} minutes.")
