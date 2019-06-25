"""
Uses API ACCESS_TOKEN
Pulls data from news api
saves to file labelled with date
"""
import json
import os
from datetime import date
from newsapi import NewsApiClient


f = open("../keys/api.txt", "r")
keys = f.read()
f.close()
ACCESS_TOKEN = keys


today = date.today()
print("Today's date:", today)

# create todays directory
if os.path.isdir("data/" + str(today)):
	print('Dir Already exists')
else:
	os.mkdir("data/" + str(today))

# Init API
newsapi = NewsApiClient(api_key=ACCESS_TOKEN)

news_keyname_array = ['BBC,bbc-news', 'abc,abc-news','cnn,cnn','fox,fox-news','independent,independent','mirror,mirror','metro,metro','rt,rt','daily_mail,daily-mail']
news_array = []

print("PULLING NEWS HEADLINES - PLEASE WAIT .......")
for item in news_keyname_array:
	print("Processing " + str(item.split(',')[0]) + " headlines")
	news_name = item.split(',')[0]
	news_key = item.split(',')[1]
	json_item = newsapi.get_top_headlines(sources=news_key)
	news_array.append(json_item)
	print("Complete - WRITING TO FILE.......")
	file_name = str("data/" + str(today) + "/" + str(news_name) + ".json")
	with open(file_name, 'w') as fp:
		json.dump(json_item, fp)

