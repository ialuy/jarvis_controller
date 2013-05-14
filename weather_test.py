## import statements
import os
from os import *
import sys
import twitter
import time
import re
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
        print ("""\n**************
weather - check the weather forecast in a specific city
news - get the latest news from @BBCBreaking
**************\n""")
        get_web_data()

    ## Weather
    elif "weather" in user_input:
        system('say Which city would you check?')
        city = raw_input("Choose city: ")
        if city == "Oslo":
            twitter_adr = oslo
        elif city == "London" :
            twitter_adr = london
        else:
            system('say Sorry, but I do not have that city.')
            sys.exit(0)
        system('say The weather forecast for ' + city + ' is')

    ## News
    elif "news" in user_input:
        twitter_adr = BBC_news
        if "please" in user_input:
            system('say Thank you for asking politely.')
        system('say The latest news from BBC are: ')

    ## Default   
    else:
        if "quit" in user_input:
            system('say Goodbye. Always a pleasure.')
            sys.exit(0)
        system('say I am sorry, but I do not understand your query.')
        sys.exit(0)

    get_data = api.GetUserTimeline(twitter_adr)
    read_data = [s.text for s in get_data]
    data_content = read_data[0]
    print(str(data_content))    
    mod_data = re.sub(r"[#&/]", "", data_content) # alter list of unwanted characters
    system('say ' + mod_data)
#endregion

get_web_data()
