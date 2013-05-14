## import statements
import os
from os import *
import twitter
import time
#endregion

## Authenticate yourself with Twitter
api = twitter.Api(consumer_key='Y7Uw0oDAojq1SyAMJY0w', consumer_secret='8Mlowssv23wDzzTIZmucj4dlmh7XT1kx1ZzKacsimTY', access_token_key='21760851-pRlUbHvzaDhDwOO1h4BS2SlLPrPGouaAB45fFvNnu', access_token_secret='xGJpM8cQ6KFOQQOhySdDtj853QgDbpJkFChMztVUjZA')

## Welcome message
system('say Testing Jarvis controlled through Twitter.')
print('Testing Jarvis controlled through Twitter.')
system('say Waiting for tweet..')
print('Waiting for tweet..')
#endregion

def jarvis_controller():
    status = []
    x = 0

    status = api.GetUserTimeline('ialuy') ## get latest tweets
    searchStatus = [s.text for s in status] ## put tweets in an array
    tweet_content = searchStatus[0].split() ## split the first tweet into words

    ## Open picture
    if tweet_content[0] == '#pi_open_pic':
        system('say I have read your Tweet.')
        system('say Opening picture.')
        os.system('open /Users/itsyulaibitch/Desktop/test_picture.png')

    ## Open text file
    elif tweet_content[0] == '#pi_open_file':
        system('say I have read your Tweet.')
        system('say Opening text file.')
        os.system('open /Users/itsyulaibitch/Desktop/testfile.txt')

    ## Check weather
    elif tweet_content[0] == '#pi_weather':
        system('say Weather forecast for Oslo is ')
        weather_source = api.GetUserTimeline('oslo_weather')
        read_weather = [s.text for s in weather_source]
        weather_content = read_weather[0]
        str(weather_content)
        # replace parentheses with white spaces in python (applies to @weatherinoslo)
        system('say '+ weather_content)
        
counter = 1
while counter <= 2:
    jarvis_controller() ## call jarvis_controller function
    time.sleep(15) ## sleep for 15 seconds to avoid rate limiting
    counter += 1
