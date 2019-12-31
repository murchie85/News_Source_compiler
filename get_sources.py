"""
find out what news sources are available 
"""
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
newsapi = NewsApiClient(api_key=ACCESS_TOKEN)
data = newsapi.get_sources()


for x in range(0, len(data['sources'])):
    print(data['sources'][x]['id'])