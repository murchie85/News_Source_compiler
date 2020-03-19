#-----------------------------------------------------------------------------------------
#
# Program name : pick_your_news.py
# Program Created Date: 26 jan 2020
# Program Amanded Date: 26 Jan 2020
# Program Author: Adam McMurchie
#
# Program Description:  This program uses news API and lets the user select the news source to review. 
#
# Input Files:     Data from news.api which is whatever was present 15 minutes ago. 
# Output Files:    Json files in data folder, output.csv full list in data folder
#
# Program Flow :  **to be updated** Run job three times per day (at least)
#                  Gets current date
#                  Checks current date data folder (create if not exist)
#                  compares news array pulled from news.api to written files
#                  If news array has items that are not in written files
#                  Regenerate news array with missing items
#                  call news api, get news for updated news array
#                  Save to json
#                  Also save all files to csv (can overwrite)
#                  Saves crossing any wires or putting the wrong list in the wrong market
#
#-----------------------------------------------------------------------------------------

import json
import os
from datetime import date
from newsapi import NewsApiClient
import time
import sys

# IMPORT API KEYS
f = open("../keys/2api.txt", "r")
keys = f.read()
f.close()
ACCESS_TOKEN = keys


#-------------------------------------------------------------------------------------------
#   PARMS SECTION 
#-------------------------------------------------------------------------------------------

# READING IN 
NewsFileNameArray = []                         # A LIST OF FILENAMES 
data = []                                      # ALL NEWS DATA FROM LOCAL NEWS JSON FILES

#-------------------------------------------------------------------------------------------
#   SELECT NEWS
#-------------------------------------------------------------------------------------------

# REQUESTING NEW DATA
newsapi = NewsApiClient(api_key=ACCESS_TOKEN)  # INITIALISING newsapi object
news_keyname_array = ['bbc-news', 'abc-news','cnn','fox-news','independent','cbs-news','metro','nbc-news', 'financial-post', 'the-new-york-times', 'al-jazeera-english', 'reuters', 'the-hill' , 'breitbart-news', 'the-verge', 'the-huffington-post', 'the-washington-post', 'wired', 'fortune', 'google-news', 'ign', 'new-scientist', 'recode', 'reddit-r-all', 'the-lad-bible', 'time', 'xinhua-net']
news_keyname_array = sorted(news_keyname_array)
print(news_keyname_array)
print('Select your news source:')
print('')
for x in range(0, len(news_keyname_array)):
    print(str(x) + ' ' + str(news_keyname_array[x]))

selection = - 1
while selection not in range(0, len(news_keyname_array)):
    selection = int(input('News Source: '))
print('')
selected_news = news_keyname_array[selection]
print('Selected News Source: ' + str(selected_news.upper()))
print('')
choice = ''
while choice != 'A' and choice != 'S' and choice != 'M':
    choice = str(input('PLEASE SELECT A PRINTOUT METHOD \n A: Auto \n S: Semi-Auto  \n M: Manual line by line \n ')).upper()

#-------------------------------------------------------------------------------------------
#   GET NEWS
#-------------------------------------------------------------------------------------------
print('Getting News')
print('')
json_item = newsapi.get_top_headlines(sources=selected_news)
articles = json_item['articles']
print(chr(27) + "[2J")
if len(articles) < 1:
    print('Fuck all news available , sorry')
print('')




#-------------------------------------------------------------------------------------------
#   PRINT NEWS
#-------------------------------------------------------------------------------------------

def med_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.035)

def fast_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)



import time
print('------------start------------------')
for news in range(0, len(articles)):
    # PRINT HEADLINE
    print('')
    if choice == 'A' or choice == 'S':
        med_print(articles[news]['title'].upper())
        time.sleep(1)
    else:
        print(articles[news]['title'].upper())
        input('')
    print('')
    # PRINT SOURCE AND AUTHOR 
    print(articles[news]['source']['name'] + ':  ' + str(articles[news]['author']))
    if choice == 'M':
        input('')
    else:
        time.sleep(1)
    print('')
    # PRINT DESCRIPTION 
    if choice == 'A' or choice == 'S':
        fast_print('SUMMARY: ' + str(articles[news]['description']))
    else:
        print('SUMMARY: ' + str(articles[news]['description']))
    
    if choice == 'M':
        input('')
    else:
        time.sleep(1)
    print('')
    print('Published at: ' + str(articles[news]['publishedAt'][0:10]))
    if choice == 'M':
        input('Press any key to continue')
    else:
        time.sleep(1)
    print('')
    print(articles[news]['url'])
    print('-----------next----------------')
    print('')
    print('')
    print('')
    if choice == 'S' or choice == 'M':
        input('Press any key to continue')
    else:
        time.sleep(2)
    print(chr(27) + "[2J")


print('News reel complete')
