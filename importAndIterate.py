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

def mapEntry(entry, index):

	#set initiating_player
	player_name = originDataFrame.loc[index, 'player']
	entry.initiate_player(player_name);

	#track coordinates, determine when Entry ends by case
	if entry.style == 'drop':
		initialX = originDataFrame.loc[index, 'x_coord_ft']
		temp_list = []
		inZone = 0
		beenInZone = 0
		for i in range(index+1, numberOfEvents):
			currentXstr = str(originDataFrame.loc[i, 'x_coord_ft'])
			currentYstr = str(originDataFrame.loc[i, 'y_coord_ft'])
			currentX = int(currentXstr)
			currentY = int(currentYstr)
			#track coordinates
			temp_list.append([currentX, currentY])
			#puck exits zone
			if currentX < 125 and beenInZone == 1:
				#stop entry, save tracked coordinates
				entry.coords = temp_list
				endTime = originDataFrame.loc[i, 'clock']
				#update time for entry
				setTime(startTime, endTime, entry)
				#update entry success
				if entry.time_in_zone >= 10:
					entry.success = True
					return i
			#check fail entry
			if currentX < initialX:
				#save tracked coordinates so far
				entry.coords = temp_list
				return i
			#puck remains zone
			if currentX > 125 and inZone == 1:
				beenInZone = 1
				continue
			#puck enters zone
			if currentX > 125:
				inZone = 1
				startTime = originDataFrame.loc[i, 'clock']
	else:
		temp_list = []
		startTime = originDataFrame.loc[index, 'clock']
		for i in range(index+1, numberOfEvents):
			currentXstr = str(originDataFrame.loc[i, 'x_coord_ft'])
			currentYstr = str(originDataFrame.loc[i, 'y_coord_ft'])
			currentX = int(currentXstr)
			currentY = int(currentYstr)
			#track coordinates
			temp_list.append([currentX, currentY])
			#check stop entry
			if currentX < 125: #flipped the inequality...I think this is right...
    			#save tracked coordinates so far
				entry.coords = temp_list
				endTime = originDataFrame.loc[i, 'clock']
                #update time for entry
				setTime(startTime, endTime, entry)
                #update entry success
				if entry.time_in_zone >= 10:
					entry.success = True
					return i
			#added this to make sure it terminates properly, not sure if it is correct...
				else:
					entry.coords = temp_list
					return i

#function to iterate through events, identify and create list of entry attempts
def findEntries():
    i = 1
    while i < numberOfEvents - 1:
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
                i = mapEntry(newEntry, i) #insert function here
                listOfEntries.append(newEntry)
                continue
            #check for a dump and chase entry
        elif currentX - previousX >= dumpThreshold and previousX <=150 and previousX >=125:
                newEntry = entry.Entry()
                newEntry.add_style("dump")
                #call function to fill in rest of entry, pass newEntry and index
                i = mapEntry(newEntry, i-1)
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
