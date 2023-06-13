"""
Iterates through data folder
appends each csv
removes duplicates
writes new CSV to base of data
"""
# IMPORT STATEMENTS 
import json
import os
import time
import sys
from sys import argv
from datetime import date, timedelta
import pandas as pd

# can passed in by program call
limit = sys.argv[-1]

today = date.today()
yesterday = date.today() + timedelta(days=-1)



# GET TARGET DIR
dir = 'data/' + str(today) + '/' + 'output.csv'
ydir = 'data/' + str(yesterday) + '/' + 'output.csv'


# PULL INTO DATA FRAME 
try:
	df = pd.read_csv(dir)
except:
	df = pd.read_csv(ydir)


df = df.sample(frac=1) # shuffle 




# ITERATE THROUGH CSV FILES
print('')
print('')
print("***************************")
print("    BREAKING NEWSFLASH     ")
print("***************************")
print('')
print('')
print(str(today))
print(' Number of articles: ' + str(df.shape[0]))
print('')
print('')
print(' HERE IS THE NEWS.......')
print('')
print('')

# PRINT TO TERMINAL
counter = 0
for index, row in df.iterrows():
	print(' *' + str(row['source']) + '*')
	print('')
	print('')
	print((str(row['title'].upper())))
	print('')
	print('')
	print(str(row['description']))
	print('')
	print('')
	print(' URL can be found here ')
	print('')
	print(row['url'])
	print('')
	print('')
	print('')
	print("******END OF ARTICLE****")
	counter +=1
	if(counter>=limit): exit()
	print('Next article...')
	print('')
	print('')


