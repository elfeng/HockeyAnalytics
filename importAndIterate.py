#file to import and parse Canucks data and iterate through to identify entry attempts
import pandas as pd
import numpy as np
import entry
import json
import datetime
import time

#import Canucks data and parse into data frame
originDataFrame = pd.read_csv('CanucksFullData.csv')
#print to check success of import, REMOVE!!
#print(originDataFrame.head())
#print(originDataFrame.tail()

#global variables
numberOfEvents = 432235
dropPassThreshold = 10
dumpThreshold = 30
listOfEntries = []

#function to iterate through events, identify and create list of entry attempts
def findEntries():
    i = 1
    while i < 100 :
        currentX = originDataFrame.loc[i, 'x_coord_ft']
        previousX = originDataFrame.loc[i-1, 'x_coord_ft']
        #check if in neutral zone
        if (75 <= currentX) and (currentX <= 125):
            #check if drop pass, dump and chase, or no entry attempt
            #check for drop pass
            if previousX - currentX >= dropPassThreshold:
                newEntry = entry.Entry()
                newEntry.add_style("drop")
                #call function to fill in rest of entry, pass newEntry and index
                i = i + 1 #insert function here
                listOfEntries.append(newEntry)
                continue
            #check for a dump and chase entry
            elif currentX - previousX >= dumpThreshold:
                newEntry = entry.Entry()
                newEntry.add_style("dump")
                #call function to fill in rest of entry, pass newEntry and index
                i = i + 1 #insert function here
                listOfEntries.append(newEntry)
                continue
        i = i + 1

#converts clock-string to seconds and updates the entries time in zone
def setTime(startTime, endTime, entry):
    start = time.strptime(startTime, "%M:%S")
    end = time.strptime(endTime, "%M:%S")
    entry.time_in_zone = (start.tm_min * 60 + start.tm_sec) - (end.tm_min * 60 + end.tm_sec)


findEntries()
print(len(listOfEntries))

#creates json object from the list of entries
jsonStringEntries = json.dumps([entry.Entry.dump() for entry.Entry in listOfEntries])
jsonEntries = json.loads(jsonStringEntries)

#dumps jsonEntries into new json file
with open("testJSON.json", "w") as outfile:
    json.dump(jsonEntries, outfile)
