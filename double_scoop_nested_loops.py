import random

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for day in day_of_week:
    for time in time_of_day:
        print(f"on {day} {time} you were feeing {random.choice(moods)}")