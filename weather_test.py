## import statements
import os
from os import *
import sys
import twitter
import time
#endregion

## Authenticate yourself with Twitter
api = twitter.Api(consumer_key='Y7Uw0oDAojq1SyAMJY0w', consumer_secret='8Mlowssv23wDzzTIZmucj4dlmh7XT1kx1ZzKacsimTY', access_token_key='21760851-pRlUbHvzaDhDwOO1h4BS2SlLPrPGouaAB45fFvNnu', access_token_secret='xGJpM8cQ6KFOQQOhySdDtj853QgDbpJkFChMztVUjZA')

## Welcome message
system('say Testing information retrieval controlled through Twitter.')
system('say What can I do for you?')
#endregion

## Setting up Twitter
status = []
x = 0
#endregion

oslo = 'oslo_weather'
london = 'BBCWeatherAlert'
BBC_news = 'BBCBreaking'

## Query weather forecast
def get_web_data():
    user_input = raw_input("What can I do: ")
    if "help" in user_input:
        system('say Here is a list of available commands')
        print ("\n**************")
        print ("weather - check the weather forecast in a specific city")
        print ("news - get the latest news from @BBCBreaking")
        print ("**************\n")
        get_web_data()
    ## Weather
    elif "weather" in user_input:
        system('say Which city would you check?')
        city = raw_input("Choose city: ")
        if city == "Oslo":
            weather_source = api.GetUserTimeline(oslo)
        elif city == "London" :
            weather_source = api.GetUserTimeline(london)    
        else:
            system('say Sorry, but I do not have that city.')
            sys.exit(0)
        system('say The weather forecast for ' + city + ' is')
        read_weather = [s.text for s in weather_source]
        weather_content = read_weather[0]
        str(weather_content)
        print(weather_content)
        # replace parentheses with white spaces in python (applies to @weatherinoslo)
        system('say '+ weather_content)

    ## News
    elif "news" in user_input:
        if "please" in user_input:
            system('say Thank you for asking politely.')
        system('say I will check the latest news.')
        news_source = api.GetUserTimeline(BBC_news)
        read_news = [s.text for s in news_source]
        news_content = read_news[0]
        str(news_content)
        print(news_content)
        system('say Latest news is ' + news_content)
    ## Default    
    else:
        system('say I am sorry, but I do not understand your query.')
#endregion

get_web_data()
