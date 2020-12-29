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

slow_print('Hello')
print('')
print('')
med_print('	¯\_(ツ)_/¯ ')
print('')
print('')
time.sleep(2)
fast_print('This program prints and streams thew news in your terminal, (Actually I am running right now, this is what I looks like!) ')
slow_print('\n')
slow_print('\n')
slow_print('')
slow_print('(◔_◔)')
fast_print('')
print('')
print('')
fast_print('My job is to keep you away from manipulative news sites, ....grrr....')
fast_print('')
print('')
slow_print('\n')
slow_print('\n')
slow_print('')
slow_print('	( º﹃º )   ୧༼ಠ益ಠ༽୨')
fast_print('')
print('')
print('')
fast_print('You can also use me by following the link in the description or looking for murchie85 on github')
print('')
print('')
slow_print('THANKS! 	\(^-^)/')
print('')
print('')
time.sleep(1)
print('')
print('')
fast_print('HERE IS THE NEWS.......')
print('')
print('')

# PRINT TO TERMINAL
y = 0 
for index, row in df.iterrows():
	y = y + 1
	med_print('*' + str(row['source']) + '*')
	print('')
	print('')
	med_print((str(row['title'].upper())))
	print('')
	print('')
	fast_print(row['description'])
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
	if y == 2:
		break
	med_print('Next article...')
	print('')
	print('')
	time.sleep(3)

print('')
print('')
med_print('PLEASE LIKE, SHARE AND SUBSCRIBE')
slow_print('\n')
slow_print('\n')
slow_print('')
slow_print('✌(-‿-)✌')
print('')
print('')
print('')
print('')

