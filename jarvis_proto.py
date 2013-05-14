## import statements
import os
from os import *
from datetime import datetime
import random
from random import randint
import time
import sys
#endregion

## Define Jarvis
system('say Testing version 1.0')
system('say Includes greeting and simple questions')
#endregion

## EXIT ##
end_message = "Like always, it has been a pleasure talking to you. Catch you later!"
def end_jarvis():
    system('say ' + end_message)
    sys.exit(0)
#endregion

## Defining time
now = datetime.time(datetime.now())

morning = now.replace(hour = 8, minute = 0, second = 0, microsecond = 0)
afternoon = now.replace(hour = 12, minute = 0, second = 0, microsecond = 0)
evening = now.replace(hour = 17, minute = 0, second = 0, microsecond = 0)
night = now.replace(hour= 22, minute = 0, second = 0, microsecond = 0)
late = now.replace(hour= 00, minute = 0, second = 0, microsecond = 0)
midnight = now.replace(hour = 23, minute = 59, second = 0, microsecond = 0)
#endregion

## Greeting based on time of day
if  now > morning and now < afternoon:
    system('say Good Morning my Lady')
elif  now > afternoon and now < evening:
    system('say Good Afternoon my Lady')
elif  now > evening and now < night:
    system('say Good Evening my Lady')
elif now > night or now < morning:
    system('say Good Night my Lady')
    system('say I hope your day was nice.')
    if now > late or now > midnight :
        system('say I believe it is time to go to bed.')
        system('say May I ask what you are doing up at this time?')
#endregion

time.sleep(1)

## Ask for user input
system('say How are you today?')
mood = raw_input("Enter mood here: ")

if "good" in mood or "well" in mood:
    system('say Good for you!')
    system('say That warms my binary heart.')
elif "bad" in mood or "sick" in mood or "down" in mood :
    system('say I am sorry to hear that.')
    system('say Sending you some digital comfort.')
elif mood == "quit":
    end_jarvis()
else :
    system('say Okay.')
    system('say We can always talk another time')
#endregion

time.sleep(1)

def social_super():
    ## SOCIAL Ask Jarvis
    def ask_jarvis_social():
        question = raw_input("Ask me: ")    
        random_state = random.randint(1, 3)

        if "how are you" in question : #mood
            if random_state == 1:
                system('say I am good as ever.')
                system('say Life is always bright inside this box.')
            elif random_state == 2:
                system('say I have been feeling a bit lonely.')
                system('say It is good to have you back')
            elif random_state == 3:
                system('say Well, to be honest. I am feeling a bit restless.')
        elif "your name" in question : #name
            system('say I do not yet have a name.')
            system('say Would you like to give me a name?')
            name = raw_input("Call me: ")
            system('say Thank you, my Lady')
            system('say From now on my name is ' + name)
        elif question == "quit":
            end_jarvis()
        else : #default
            system('say I am sorry but I do not understand your question.')
            system('say Would you like to try that again?')
            ask_again = raw_input("y/n: ")
            if ask_again == "yes" or ask_again == "y":
                system('say Ask me again.')
                ask_jarvis_social()
            else:
                system('say Okay. Talk to you later.')
            
    system('say Feel free to ask me anything!')
    ask_jarvis_social()
    #endregion
#endregion

## Productive Super
def productive_super():
    ## PRODUCTIVE Ask Jarvis
    def ask_jarvis_productive():
        query = raw_input("Task to complete: ")
        if query == "help":
            system('say Here is a list of available commands:')
            print("\n***********")
            print("weather - check forecast")
            print("calendar - check appointments")
            print("***********\n")
            ask_jarvis_productive()
        elif "weather" in query : #weather
            system('say I will check the weather forecast.')
        elif "appointments" in query or "calendar" in query or "schedule" in query :
            system('say I will check your calendar for you.')
        elif query == "quit":
            end_jarvis()
        else :
            system('say I am sorry but I do not understand your question.')
            system('say Would you like to try that again?')
            ask_again = raw_input("y/n: ")
            if ask_again == "yes" or ask_again == "y":
                system('say Ask me again.')
                ask_jarvis_productive()
            else:
                system('say Okay. Talk to you later.')
                
    system('say What can I do for you?')
    ask_jarvis_productive()
    #endregion
#endregion

## MAIN
system('say Shall we discuss pleasure or business?')
user_input = raw_input("social/productive: ")
if user_input == "social":
    social_super()
elif user_input == "productive":
    productive_super()
elif user_input == "quit":
    end_jarvis()
else:
    system('say I am sorry, but I do not understand.')
