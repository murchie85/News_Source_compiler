"""
Iterates through data folder
appends each csv
removes duplicates
writes new CSV to base of data
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



# ITERATE THROUGH CSV FILES

print("Pulling data from storage......")

# ======================== collate to array
directory = "data/"
selected_files = []

full = pd.DataFrame
imported = []
for directory in os.listdir(directory):
    if directory == '.DS_Store':
        continue
    print(directory)
    imported = pd.read_csv("data/" + directory + "/" + 'output.csv', index_col=0)
    print('The size of directory ' + str(directory) + ' is : ' + str(imported.shape))
    if full.empty:
        full = imported
    else:
        full = full.append(imported)


print('Shape of combined directories is : ')
print(full.shape)
print('')
print('removing duplicates')
full = full.drop_duplicates(subset='title', keep='first')
print('final size of data is ')
print(full.shape)
print('')
print('Saving to file')
full.to_csv('full_data.csv')