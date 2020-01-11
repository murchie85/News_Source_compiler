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
from datetime import date, timedelta
import pandas as pd

today = date.today()
yesterday = date.today() + timedelta(days=-1)



# GET TARGET DIR
dir = 'data/' + str(today) + '/' + 'output.csv'


# PULL INTO DATA FRAME 
df = pd.read_csv(dir)
df = df.sample(frac=1) # shuffle 



# BUFFER PRINT

def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)


def med_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

def fast_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def superfast_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)



# ITERATE THROUGH CSV FILES
print('')
print('')
print("**********************************************************************************************")
time.sleep(1)
print("                                  BREAKING NEWSFLASH                                          ")
time.sleep(1)
print("**********************************************************************************************")
print('')
print('')

fast_print('HERE IS THE NEWS.......')
print('')
print('')

# PRINT TO TERMINAL

for index, row in df.iterrows():
	med_print('*' + str(row['source']) + '*')
	print('')
	print('')
	med_print((str(row['title'].upper())))
	print('')
	print('')
	fast_print(str(row['description']))
	print('')
	time.sleep(0.8)
	print('')
	superfast_print('URL can be found below')
	print('')
	time.sleep(0.8)
	superfast_print(row['url'])
	print('')
	print('')
	print('')
	print("********************************************END OF ARTICLE**************************************************")
	med_print('Next article...')
	print('')
	print('')
	time.sleep(3)


