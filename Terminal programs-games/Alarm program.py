# Use: https://www.timeanddate.com/worldclock/egypt/cairo

import time
import datetime
import pygame

# ===========================================================
# ALARM CLOCK PROGRAM (24-HOUR FORMAT)
# -----------------------------------------------------------
# This script allows the user to set an alarm in 24-hour format.
# When the current system time matches the alarm time, a sound plays.
# The program uses pygame's mixer module to handle audio playback.
# ===========================================================

def set_alarm(alarm_time):
    print(f"Alarm is set for: {alarm_time}\n")
    
    # Path to the alarm sound file
    alarm_sound = "C:/Users/A.R/Documents/PROGRAMMING/pythonData/Media/my_alarm_sound.mp3"

    # Infinite loop to constantly check the current time against the alarm time
    while True:
        # Get the current system time in "HH:MM:SS" format
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        # Check if current time matches the user-set alarm time
        if alarm_time == current_time:
            print("\nWake up!! 😪")

            # Initialize pygame mixer to play the sound
            pygame.mixer.init()
            pygame.mixer.music.load(alarm_sound)  # Load the chosen alarm sound
            pygame.mixer.music.play()             # Start playing the alarm sound

            # Inner loop to keep the program alive until the sound finishes playing
            while pygame.mixer.music.get_busy():
                # get_busy() returns True while music is playing
                # Sleep 1 second between checks to prevent CPU overuse
                time.sleep(1)
                
            break

        # Sleep 1 second between checks to avoid high CPU usage
        time.sleep(1)


if __name__ == '__main__':
    alarm_time = input("\nSet an alarm (HH:MM:SS): ")
    print('-' * 50)
    set_alarm(alarm_time)


# https://www.youtube.com/watch?v=uf8DvQlWm7M&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=76