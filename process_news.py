#-----------------------------------------------------------------------------------------
#
# Program name : process_news.py
# Program Created Date: 31 December 2019
# Program Amanded Date: 31 December 2019
# Program Author: Adam McMurchie
#
# Program Description:  This program iterrogates news.api, pulls data and consolodates in a re-occuring append fasion. The aim to 
#                       Overtime build a portfolio of news data from various sources. Various archival, and time delay considerations 
#                       have been baked into the code (explained in program flow).
#
# Input Files:         Data from news.api which is whatever was present 15 minutes ago. 
# Output Files: 
#
# Program Flow :   Run job three times per day (at least)
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



# IMPORT STATEMENTS 
import json
import os
from datetime import date
from newsapi import NewsApiClient
import pandas as pd

# IMPORT API KEYS
f = open("../keys/api.txt", "r")
keys = f.read()
f.close()
ACCESS_TOKEN = keys


#-------------------------------------------------------------------------------------------
#   PARMS SECTION 
#-------------------------------------------------------------------------------------------

# READING IN 
NewsFileNameArray = []                         # A LIST OF FILENAMES 
data = []                                      # ALL NEWS DATA FROM LOCAL NEWS JSON FILES

# REQUESTING NEW DATA
newsapi = NewsApiClient(api_key=ACCESS_TOKEN)  # INITIALISING newsapi object
news_keyname_array = ['bbc-news', 'abc-news','cnn','fox-news','independent','mirror','metro','daily-mail', 'Theguardian.com' , 'Sky.com', 'the-new-york-times', 'al-jazeera-english', 'reuters', 'the-hill' , 'breitbart-news', 'the-verge', 'the-huffington-post']
news_array = []


#-------------------------------------------------------------------------------------------
#   READING LOCAL FILES 
#-------------------------------------------------------------------------------------------
# GET TODAYS DATE 
today = date.today()
print("Today's date:", today)

# CREATE A NEW DIRECTORY FOR TODAY IF NOT EXIST
if os.path.isdir("data/" + str(today)):
	print('Dir Already exists')
else:
	os.mkdir("data/" + str(today))

print('')

# ITERATE THROUGH DATA FOLDER
directory = "data/" + str(today)
for filename in os.listdir(directory):
    if filename.endswith(".json"): 
        newsName = filename[:-5]
        NewsFileNameArray.append(newsName)
        with open(str(directory) + "/" + str(filename)) as json_file:
            data.append(json.load(json_file))
        continue
    else:
        continue


print('The news sources already obtained for this day are: ')
print(NewsFileNameArray)
print('')
print('the number of saved sources are: ')
print(len(data))



#-------------------------------------------------------------------------------------------
#   UPDATING ARRAY
#-------------------------------------------------------------------------------------------


#   ONLY MAKE CALLS FOR NEWS SOURCES WE DON'T ALREADY HAVE 
#   (THIS MEANS UPDATING OUR ARRAY TO REMOVE ALREADY EXISTING SAVED NEWS SOURCES)

for item in NewsFileNameArray:
    print('removing ' + str(item))
    news_keyname_array.remove(str(item))


if not news_keyname_array:
    print('All data obtained for today, exiting.')
    exit()

print('The sources still required are ' + str(news_keyname_array))
print('')



#-------------------------------------------------------------------------------------------
#   REQUESTING MORE NEWS 
#-------------------------------------------------------------------------------------------

# Init API
print('PULLING NEWS HEADLINES - PLEASE WAIT .... ')
print('')
for item in news_keyname_array:
    print('processing ' + str(item + ' headlines'))
    news_key = item
    json_item = newsapi.get_top_headlines(sources=news_key)
    if json_item['totalResults'] == 0:
        print("Request for the " + str(item) + " news source is empty, skipping")
        print('')
        continue
    news_array.append(json_item)
    print('COMPLETE - writing to file .......')
    print('')
    file_name= str("data/" + str(today) + "/" + str(news_key) + ".json")
    with open(file_name, 'w') as fp:
        json.dump(json_item, fp)

        
#-------------------------------------------------------------------------------------------
#   BUILDING REPORT 
#-------------------------------------------------------------------------------------------

# BUILD A PANDAS DATA FRAME 
df = pd.DataFrame(columns=['source','author','title','description','url', 'requested_date','publishedAt','content'])

# CLEAR OUT DATA ARRAY AND REPOPULATE WITH NEW UPDATED JSON FILES (COULD BE MORE EFFICIENT BUT MEH)

data = []

# ITERATE THROUGH DATA FOLDER
directory = "data/" + str(today)
for filename in os.listdir(directory):
    if filename.endswith(".json"): 
        newsName = filename[:-5]
        NewsFileNameArray.append(newsName)
        with open(str(directory) + "/" + str(filename)) as json_file:
            data.append(json.load(json_file))
        continue
    else:
        continue


# Iterate through data array and write to csv

x = 0 
for news_outlet in range (0, len(data)):
    for article_number in range (0, len(data[news_outlet]['articles'])):
        source         = data[news_outlet]['articles'][article_number]['source']['name']
        author         = data[news_outlet]['articles'][article_number]['author']
        title          = data[news_outlet]['articles'][article_number]['title']
        description    = data[news_outlet]['articles'][article_number]['description']
        url            = data[news_outlet]['articles'][article_number]['url']
        publishedAt    = data[news_outlet]['articles'][article_number]['publishedAt']
        requested_date = today
        content        = data[news_outlet]['articles'][article_number]['content']
        df = df.append([{ 'source': source, 'author': author, 'title': title, 'description': description, 'url':url, 'publishedAt': publishedAt, 'requested_date': requested_date, 'content': content    }])
        x = x + 1 

print('PROCESSING COMPLETE')
print('number of articles processed are : ' + str(x))

        
df.to_csv("data/" + str(today) + "/" + 'output.csv')