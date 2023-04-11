"""
Hi There,

This Program Just For Make A Small Idea How Make Timer By Using time, 

I hope it is understandable enough,

All The Best

"""

import time

# Countdown clock
def countDown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Timer
def timerSeconds(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Run Program
countDown(1)        # countdown for 5 minutes
timerSeconds(0)     # timer for seconds