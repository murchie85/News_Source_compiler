import os
import json
from datetime import date

today = date.today()
print("Today's date:", today)


newsNameArray = []
data = []
directory = "data/" + str(today)
for filename in os.listdir(directory):
    if filename.endswith(".json"): 
        newsName = filename[:-5]
        newsNameArray.append(newsName)
        with open(str(directory) + "/" + str(filename)) as json_file:
            data.append(json.load(json_file))
        continue
    else:
        continue


print(newsNameArray)
print(len(data))