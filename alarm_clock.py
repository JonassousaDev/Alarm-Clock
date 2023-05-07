from playsound import playsound
import time 

CLEAR = '\033[2J' # corrected the escape code for clearing the terminal
CLEAR_AND_RETURN = '\033[H'

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600
        minutes_left = (time_left % 3600) // 60
        seconds_left = time_left % 60

        # added the escape codes for clearing the terminal and resetting the cursor position
        print(f'{CLEAR}{CLEAR_AND_RETURN}Alarm will sound in: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}', end='', flush=True)

    # play the alarm sound after the timer is done
    playsound('Alarm.mp3')

# get input from the user for the timer duration
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

# convert the hours, minutes, and seconds to total seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

# start the timer
alarm(total_seconds)
