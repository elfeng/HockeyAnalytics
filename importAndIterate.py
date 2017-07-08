#file to import and parse Canucks data and iterate through to identify entry attempts
import pandas as pd
import numpy as np
import entry

#import Canucks data and parse into data frame
originDataFrame = pd.read_csv('CanucksFullData.csv')
#print to check success of import, REMOVE!!
print(originDataFrame.head())
print(originDataFrame.tail())

#global variables
numberOfEvents = 432235
dropPass

#function to iterate through events, identify and create list of entry attempts
def findEntries:
    for i in range(1, numberOfEvents):
        currentX = originDataFrame.loc[i, x_coord_ft]
        previousX = originDataFrame.loc[i-1, x_coord_ft]
        #check if in neutral zone
        if 75 <= currentX && currentX <= 125:
            #check if drop pass, dump and chase, or no entry attempt
            #check for drop pass
            if
