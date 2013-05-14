## Alarm Clock

## import statements
import os
from os import *
from datetime import datetime
import random
from random import randint
import time
#endregion

system('say I am testing a new alarm clock for you')
system('say This is version 1.0')
system('say Includes setting an alarm, and a simple wake up message')

def set_alarm():
    system('say At what hour do you want to wake up?')
    global alarm_HH
    alarm_HH = raw_input("Enter hour: ")
    system('say At what minute do you want to wake up?')
    global alarm_MM
    alarm_MM = raw_input("Enter minute: ")

    system('say Do you want to wake up at ' + alarm_HH + alarm_MM)
    user_input = raw_input("y/n:")
    if user_input == "yes" or user_input == "y":
        global alarm_on
        alarm_on = True
        system('say Okay, I will wake you up then.')
    else:
        alarm_on = False
        system('say Okay. No alarm then.')
        system('say Would you like to try that again?')
        user_answer = raw_input("y/n:")
        if user_answer == "yes" or user_answer == "y" :
            set_alarm()
        else:
            system('say Okay. Talk to you later')

set_alarm()

while alarm_on:
    now = time.localtime()
    if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
        ## play sound
        system('say Time to wake up')
        system('say Remind me to get a sound for your alarm.')
        break
