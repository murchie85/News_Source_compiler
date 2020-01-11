# NEWS HEADLINE COMPILER 

![NEWS](http://fivebars.co.uk/wp-content/uploads/2018/08/news-1.jpg)

 - [Overview](#OVERVIEW)
 - [Instructions](#INSTRUCTIONS)
 - [Pip Requirements](#PIP-REQUIREMENTS)
 - [Selected Sources](#SELECTED-NEWS-SOURCES)
 - [Available Sources](#AVAILABLE-NEWS-SOURCES)
 - [Programatic News Streaming](#PROGRAMATIC-NEWS-STREAMING)

# OVERVIEW

This project utilises the awesome  [newsAPI](https://newsapi.org/s/uk-news-api) , to pull down the latest news articles, descriptions and other information from a select amount of news sources. This project then compiles those lists into a daily folder, as the API can only get a select slice of the news, it will run three times a day to build up news data which in the future could be used to drive text generation, news comparisons and so on.

Because the API returns json, it's easier to just save json files for each source, then collate those files into one CSV. This can then be appeneded throughout the day, week and year.  


This project is fully open source and mostly for fun, if any future work is aimed at generating revenue, you must comply with the newsAPI policy and upgrade from Developer. I may do this if I find a useful business case based upon my exploration here. 

 There is incomplete code you can ignore in `quiz_incomplete` folder.
  

## INSTRUCTIONS

1. Sign up to [newsAPI](https://newsapi.org/s/uk-news-api), generate keys **(it will tell you how to)** and store in a parent directory of this one called `keys`, or simply change the key path in the python code. 
2. Create a folder called `data` at same level as the python code
3. run `python process_news.py` from command line / terminal.
4. Program will pull down news articles and store them in data folder, creating a new folder for each day you run it. 

  
## PIP REQUIREMENTS

Python Version `3.7.3`
```
pandas
json
os
datetime
newsapi-python
```


## SELECTED NEWS SOURCES 

I may change this depending on the circumstance.


```
news_keyname_array = ['bbc-news', 'abc-news','cnn','fox-news','independent','mirror','metro','daily-mail', 'Theguardian.com' , 'Sky.com', 'the-new-york-times', 'al-jazeera-english', 'reuters', 'the-hill' , 'breitbart-news', 'the-verge', 'the-huffington-post']
```

## AVAILABLE NEWS SOURCES

From calling `the get_sources.py` code i have written (because the website doesn't give a full list), the below list of available ones are there. May have different ones depending on time of day? 

```
abc-news-au
aftenposten
al-jazeera-english
ansa
argaam
ars-technica
ary-news
associated-press
australian-financial-review
axios
bbc-news
bbc-sport
bild
blasting-news-br
bleacher-report
bloomberg
breitbart-news
business-insider
business-insider-uk
buzzfeed
cbc-news
cbs-news
cnbc
cnn
cnn-es
crypto-coins-news
der-tagesspiegel
die-zeit
el-mundo
engadget
entertainment-weekly
espn
espn-cric-info
financial-post
focus
football-italia
fortune
four-four-two
fox-news
fox-sports
globo
google-news
google-news-ar
google-news-au
google-news-br
google-news-ca
google-news-fr
google-news-in
google-news-is
google-news-it
google-news-ru
google-news-sa
google-news-uk
goteborgs-posten
gruenderszene
hacker-news
handelsblatt
ign
il-sole-24-ore
independent
infobae
info-money
la-gaceta
la-nacion
la-repubblica
le-monde
lenta
lequipe
les-echos
liberation
marca
mashable
medical-news-today
msnbc
mtv-news
mtv-news-uk
national-geographic
national-review
nbc-news
news24
new-scientist
news-com-au
newsweek
new-york-magazine
next-big-future
nfl-news
nhl-news
nrk
politico
polygon
rbc
recode
reddit-r-all
reuters
rt
rte
rtl-nieuws
sabq
spiegel-online
svenska-dagbladet
t3n
talksport
techcrunch
techcrunch-cn
techradar
the-american-conservative
the-globe-and-mail
the-hill
the-hindu
the-huffington-post
the-irish-times
the-jerusalem-post
the-lad-bible
the-new-york-times
the-next-web
the-sport-bible
the-times-of-india
the-verge
the-wall-street-journal
the-washington-post
the-washington-times
time
usa-today
vice-news
wired
wired-de
wirtschafts-woche
xinhua-net
ynet
```

# PROGRAMATIC NEWS STREAMING


In order to get this working, you need to have news data saved locally *(in future I will show a streaming option, which is really easy but will abuse the limit restrictions news api enforces, so best to run locally)*.    

**IF YOU HAVEN'T FOLLOWED ANY OF THE INSTRUCTIONS ABOVE THEN...**

1. Clone this repo
2. CD into the repo and create a data folder
3. Run `python process_news.py` this will pull news down into your data folder and label it with todays date.
4. Run `python terminal_newsFlash.py` this will now do the news reporting :) 
  
You will still need to install dependencies from the `PIP REQUIREMENTS` section and also sign up to news API (shown above in instructions section).
Depending on your needs you might like me want to schedule `process_news.py` a couple of times a day to build the news up ready to go (I do this as I plan to perform analysis on historical data).



# COMMON ISSUES

If you get a traceback issue like below: 

```
Traceback (most recent call last):
  File "process_news.py", line 33, in <module>
    from newsapi import NewsApiClient
ImportError: cannot import name NewsApiClient
```
  
Then you may want to change the `process_news.py` file import statement from `from newsapi import NewsApiClient` to `from newsapi.newsapi_client import NewsApiClient` . 
   

If you get the following similar error:
```
File "process_news.py", line 37, in <module>
    f = open("../keys/api.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: '../keys/api.txt'
```
  
  
You need to sign up to newsapi and download the keys, you can do that [here](https://newsapi.org/) 


**Powered by news API**
[link](https://newsapi.org/s/uk-news-api)