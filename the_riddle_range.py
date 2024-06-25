# task 1
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    print(f"On {day}, you were feeling {random.choice(moods)}")

# tried using the range() function and couldnt get it to work. So i went back and simplified it. I believe it still works as the assignment intended. If you could please explain to me how I could use the range() function in this example that would be of great help.
# below is the code I tried before, using range()
# import random

# moods = ["Happy", "Sad", "Energetic", "Calm"]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# for day in range(len(days)):
    # print(f"On {day}, you were feeling {random.choice(moods)}")
