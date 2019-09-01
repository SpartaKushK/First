'''
Alarm Clock/Timer
'''

import winsound
import time


def alarm_clock():
    frequency = 2500  # Set Frequency (Hertz)
    duration = 1000  # Set Duration (Seconds)
    base_time = 0  # Basecount for
    start_timer = input('Start? Please enter y/n: ')
    mins = int(input('How long do you want to set a alarm for (in minutes)? '))

    if start_timer == 'y':

        while base_time != mins:
            print(str(base_time) + 'minutes has passed'), mins  # Just show how much time has passed
            time.sleep(60)  # To count up by a minute
            base_time += 1  # Add to x to reach mins
            continue  # Repeat

        else:
            for i in range(8):  # Repeat the beeping 8 times
                winsound.Beep(frequency, duration)  # Make beep sounds
                time.sleep(0.5)  # Time inbetween each beep

alarm_clock()  # Call function to run
