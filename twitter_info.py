## import statements
import os
from os import *
import sys
import twitter
import time
import re
#endregion

## Authenticate yourself with Twitter
api = twitter.Api(consumer_key='consumer_key', consumer_secret='consumer_secret', access_token_key='access_token_key', access_token_secret='access_token_secret')

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
weather - get the latest weather report for a specific city
news - get the latest news from @BBCBreaking
persona - get the lastest updates from a specified twitter account
**************\n""")
        get_web_data()

    ## Weather
    elif "weather" in user_input and "news" not in user_input:
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
    elif "news" in user_input and "weather" not in user_input:
        twitter_adr = BBC_news
        if "please" in user_input:
            system('say Thank you for asking politely.')
        system('say The latest news from BBC are: ')

    ## Request twitter username
    elif "personal" in user_input:
        system('say Which user do you want me to check?')
        twitter_adr = raw_input("Enter twitter user here: ")
        system('say Okay, the latest tweet from ' + twitter_adr + ', is')

    ## Default   
    else:
        if "quit" in user_input:
            system('say Goodbye. Always a pleasure.')
            sys.exit(0)
        system('say I am sorry, but I do not understand your query.')
        sys.exit(0)

    ## GET Twitter status
    get_data = api.GetUserTimeline(twitter_adr) ## get information from user
    read_data = [s.text for s in get_data] ## organise twitter statuses into array
    data_content = read_data[0] ## get the first item of the array
    print(str(data_content)) ## print original tweet
    mod_data = re.sub(r"[(#&);]", "", data_content) ## remove unwanted characters
    system('say ' + mod_data) ## read tweet
#endregion

get_web_data()
