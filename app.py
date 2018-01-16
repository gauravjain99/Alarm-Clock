import webbrowser
import time
import Alarm
import random

# This alarm program can set the alarm for today only.

print("The current time and date is ",time.asctime(), "now please enter the following details to set an alarm\n")
print("You can set ringtone of your own choice or you can try our 'random' collection")

while True:
    try:
        choice = int(input('Enter 1 or 2 to select\n1 Your own url\n2 Wanna try the random collection : '))

        if choice == 1:
            url = input('Please enter the url : ')
        elif choice == 2:
            lines = open('music_files.txt').read().splitlines()
            url = random.choice(lines)
            break
    except:
        print("Please enter 1 or 2")

set_alarm = Alarm.alarm()

selected_time = time.strftime("%a %b %d %H:%M:%S %Y",set_alarm)
integer_selected_time = selected_time[8:10]
integer_selectedtime = int(integer_selected_time)
print(integer_selectedtime)

if integer_selectedtime < 10:
    main_time = selected_time[:8]+" " +selected_time[9:]
else:
    main_time = selected_time
print("Alarm set for ",main_time)
current_time = time.asctime()

def play():
    webbrowser.open(url)


while True:
    if not main_time == current_time:
        current_time = time.asctime() # to update the value of current_time every second 
        continue
    play()
    break
